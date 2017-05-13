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
    with Img(fp=path(image['sub'])) as src, TemporaryFile() as tf:
        src.convert('L')
        src.save(fp=tf)
        with Img(fp=tf) as dest:
            assert (dest.mode, dest.n_frames) == image['res']
