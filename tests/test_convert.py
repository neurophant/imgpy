from tempfile import TemporaryFile

import pytest

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'res': ('P', 38)
}, {
    'sub': 'anima/clear.gif',
    'res': ('P', 12)
}, {
    'sub': 'fixed/bordered.jpg',
    'res': ('L', 1)
}, {
    'sub': 'fixed/clear.jpg',
    'res': ('L', 1)
}, ))
def test_convert(path, image):
    with Img(fp=path(image['sub'])) as src:
        src.convert('L')
        with TemporaryFile() as tf:
            src.save(fp=tf)
            tf.seek(0)
            with Img(fp=tf) as dest:
                res = (dest.mode, dest.n_frames)
    assert res == image['res']
