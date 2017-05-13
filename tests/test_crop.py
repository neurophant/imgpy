from tempfile import TemporaryFile

import pytest

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'box': (80, 40, 400, 225),
    'res': (320, 185, 38)
}, {
    'sub': 'anima/clear.gif',
    'box': (100, 50, 400, 215),
    'res': (300, 165, 12)
}, {
    'sub': 'fixed/bordered.jpg',
    'box': (25, 25, 225, 225),
    'res': (200, 200, 1)
}, {
    'sub': 'fixed/clear.jpg',
    'box': (5, 25, 505, 325),
    'res': (500, 300, 1)
}, ))
def test_crop(path, image):
    with Img(fp=path(image['sub'])) as src, TemporaryFile() as tf:
        src.crop(image['box'])
        src.save(fp=tf)
        with Img(fp=tf) as dest:
            assert (dest.width, dest.height, dest.n_frames) == image['res']
