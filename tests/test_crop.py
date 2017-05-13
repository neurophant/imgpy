from tempfile import TemporaryFile

import pytest

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'box': (80, 40, 400, 225),
}, {
    'sub': 'anima/clear.gif',
    'box': (100, 50, 400, 215),
}, {
    'sub': 'fixed/bordered.jpg',
    'box': (25, 25, 225, 225),
}, {
    'sub': 'fixed/clear.jpg',
    'box': (5, 25, 505, 325),
}, ))
def test_crop(path, image):
    with Img(fp=path(image['sub'])) as src, TemporaryFile() as tf:
        src.crop(image['box'])
        src.save(fp=tf)
        with Img(fp=tf) as dest:
            assert (dest.width, dest.height, dest.n_frames) == \
                (image['box'][2] - image['box'][0], image['box'][3] - image['box'][1], src.n_frames)
