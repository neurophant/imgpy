from functools import wraps

from PIL import Image
from PIL.ImageSequence import Iterator

__author__ = 'Anton Smolin'
__copyright__ = 'Copyright (C) 2017 Anton Smolin'
__license__ = 'MIT'
__version__ = '1.0.0'


class Img:
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
    __METHODS = ('convert', 'crop', 'filter', 'paste', 'resize', 'rotate',
                 'thumbnail', 'transform', 'transpose')

    __fp = None
    __image = None
    __frames = None

    @property
    def format(self):
        return self.__image.format

    @property
    def width(self):
        if not self.__frames:
            return self.__image.width

        return self.__frames[0].width

    @property
    def height(self):
        if not self.__frames:
            return self.__image.height

        return self.__frames[0].height

    @property
    def mode(self):
        if not self.__frames:
            return self.__image.mode

        return self.__frames[0].mode

    @property
    def mode_desc(self):
        return self.__MODES.get(self.mode)

    @property
    def n_frames(self):
        if self.__frames:
            return len(self.__frames)

        try:
            return self.__image.n_frames
        except AttributeError:
            return 1

    @property
    def animated(self):
        return self.n_frames > 1

    @property
    def frames(self):
        if self.__frames is None:
            self.__frames = [frame.copy() for frame in Iterator(self.__image)]

        return self.__frames

    def __init__(self, *, fp):
        self.__fp = fp
        self.__image = Image.open(fp)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __getattr__(self, name):
        if name not in self.__METHODS:
            raise AttributeError

        def proxy(*args, **kwargs):
            for index, frame in enumerate(self.frames):
                res = getattr(frame, name)(*args, **kwargs)
                if isinstance(res, Image.Image):
                    self.__frames[index] = res

        return proxy

    def save(self, *, fp):
        if not self.frames:
            return

        options = {'save_all': True, 'append_images': self.__frames[1:]} \
            if self.format == 'GIF' and self.animated else {}

        self.__frames[0].save(fp, format=self.format, **options)

    def close(self):
        self.__image.close()
