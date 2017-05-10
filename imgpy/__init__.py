from functools import wraps

from PIL import Image
from PIL.ImageSequence import Iterator

__author__ = 'Anton Smolin'
__copyright__ = 'Copyright (C) 2017 Anton Smolin'
__license__ = 'MIT'
__version__ = '0.1.0'


def _lazy_load(func):
    def wrapped(self, *args, **kwargs):
        self._load()

        return func(self, *args, **kwargs)

    return wrapped


class ImgInfo:
    __MODES = {
        '1': 'black and white',
        'L': 'grayscale',
        'LA': 'grayscale with transparency',
        'P': 'color palette',
        'RGB': 'true color',
        'RGBA': 'true color with transparency',
        'RGBX': 'true color with padding',
        'RGBa': 'true color with premultiplied alpha',
        'CMYK': 'color separation',
        'YCbCr': 'color video',
        'LAB': 'l*a*b color space',
        'HSV': 'hue, saturation, value color space',
        'I': 'signed integer pixels',
        'F': 'floating point pixels'
    }

    format = None
    width = None
    height = None
    mode = None
    frames = None

    @property
    def animated(self):
        return self.frames > 1

    def __init__(self, *, image):
        if isinstance(image, Img):
            frame = image.frame(index=0)

            self.format = image.info.format
            self.width = frame.width
            self.height = frame.height
            self.mode = (frame.mode, self.__MODES.get(frame.mode))
            self.frames = image.info.frames
        else:
            self.format = image.format
            self.width = image.width
            self.height = image.height
            self.mode = (image.mode, self.__MODES.get(image.mode))

            try:
                self.frames = image.n_frames
            except AttributeError:
                self.frames = 1


class Img:
    __METHODS = ('convert', 'crop', 'filter', 'paste', 'resize', 'rotate',
                 'thumbnail', 'transform', 'transpose')

    __image = None
    __info = None
    __frames = None

    @property
    def info(self):
        if self.__info is None:
            self.__info = ImgInfo(image=self.__image)

        return self.__info

    def __init__(self, *, fp):
        self.__image = Image.open(fp)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def _load(self):
        if self.__frames is None:
            self.__frames = [frame.copy() for frame in Iterator(self.__image)]

    def __getattr__(self, name):
        if name not in self.__METHODS:
            raise AttributeError

        def proxy(*args, **kwargs):
            self._load()

            for index, frame in enumerate(self.__frames):
                res = getattr(frame, name)(*args, **kwargs)
                if isinstance(res, Image.Image):
                    self.__frames[index] = res

            self.__info = ImgInfo(image=self)

        return proxy

    @_lazy_load
    def frame(self, *, index):
        return self.__frames[index]

    @_lazy_load
    def frames(self):
        for frame in self.__frames:
            yield frame

    @_lazy_load
    def update(self, *, index, frame):
        self.__frames[index] = frame

    @_lazy_load
    def save(self, *, fp):
        options = {'save_all': True, 'append_images': self.__frames[1:]} \
            if self.info.format == 'GIF' and self.info.animated else {}

        self.__frames[0].save(fp, format=self.info.format, **options)

    def close(self):
        self.__image.close()
