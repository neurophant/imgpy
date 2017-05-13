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
    with Img(fp=path(image['sub'])) as src:
        src.resize(image['size'])
        with TemporaryFile() as tf:
            src.save(fp=tf)
            tf.seek(0)
            with Img(fp=tf) as dest:
                res = (dest.width, dest.height)
    assert res == image['size']
