from tempfile import TemporaryFile

import pytest

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'size': (100, 100)
}, {
    'sub': 'anima/clear.gif',
    'size': (100, 100)
}, {
    'sub': 'fixed/bordered.jpg',
    'size': (100, 100)
}, {
    'sub': 'fixed/clear.jpg',
    'size': (100, 100)
}, ))
def test_resize(path, image):
    with Img(fp=path(image['sub'])) as src, TemporaryFile() as tf:
        src.resize(image['size'])
        src.save(fp=tf)
        with Img(fp=tf) as dest:
            assert (dest.width, dest.height,
                    dest.frame_count) == image['size'] + (src.frame_count, )
