from PIL import Image, ImageSequence


__author__ = 'Anton Smolin'
__copyright__ = 'Copyright (C) 2017 Anton Smolin'
__license__ = 'MIT'
__version__ = '0.1.0'


class ImgPyInfo:
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
        'F': 'floating point pixels'}

    format = None
    width = None
    height = None
    mode = None
    frames = None
    animated = None

    def __init__(self, *, image):
        if isinstance(image, ImgPy):
            frame = image.frame(index=0)
            self.format = image.info.format
            self.width = frame.width
            self.height = frame.height
            self.mode = (frame.mode, self.__MODES.get(frame.mode))
            self.frames = image.info.frames
            self.animated = image.info.animated
        else:
            self.format = image.format
            self.width = image.width
            self.height = image.height
            self.mode = (image.mode, self.__MODES.get(image.mode))
            try:
                self.frames = image.n_frames
            except AttributeError:
                self.frames = 1
            self.animated = self.frames > 1


class ImgPy:
    __image = None
    __info = None
    __frames = None

    def __init__(self, *, fp):
        self.__image = Image.open(fp)

    @property
    def info(self):
        if self.__info is None:
            self.__info = ImgPyInfo(image=self.__image)

        return self.__info

    def frame(self, *, index):
        return self.__frames[index]

    def frames(self):
        for frame in self.__frames:
            yield frame

    def __load(self):
        if self.__frames is not None:
            return

        self.__frames = [frame.copy()
                         for frame in ImageSequence.Iterator(self.__image)]

    def crop(self, *, box):
        self.__load()

        for index, frame in enumerate(self.__frames):
            self.__frames[index] = frame.crop(box=box)

        self.__info = ImgPyInfo(image=self)

    def resize(self, *, size, resample=0):
        self.__load()

        for index, frame in enumerate(self.__frames):
            self.__frames[index] = frame.resize(size, resample=resample)

        self.__info = ImgPyInfo(image=self)

    def thumbnail(self, *, size, resample=3):
        self.__load()

        for frame in self.__frames:
            frame.thumbnail(size, resample=resample)

        self.__info = ImgPyInfo(image=self)

    def save(self, *, fp):
        self.__load()

        options = {'save_all': True, 'append_images': self.__frames[1:]} \
            if self.info.format == 'GIF' and self.info.animated else {}

        self.__frames[0].save(fp, format=self.info.format, **options)
