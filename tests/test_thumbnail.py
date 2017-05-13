from tempfile import TemporaryFile

import pytest

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'size': (100, 100),
    'res': (100, 55)
}, {
    'sub': 'anima/clear.gif',
    'size': (100, 100),
    'res': (100, 53)
}, {
    'sub': 'fixed/bordered.jpg',
    'size': (100, 100),
    'res': (100, 100)
}, {
    'sub': 'fixed/clear.jpg',
    'size': (100, 100),
    'res': (100, 68)
}, ))
def test_thumbnail(path, image):
    with Img(fp=path(image['sub'])) as src, TemporaryFile() as tf:
        src.thumbnail(image['size'])
        src.save(fp=tf)
        with Img(fp=tf) as dest:
            assert (dest.width, dest.height,
                    dest.n_frames) == image['res'] + (src.n_frames, )
