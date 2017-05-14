from tempfile import TemporaryFile

import pytest

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'convert': 'L',
    'mode': 'P'
}, {
    'sub': 'anima/clear.gif',
    'convert': 'L',
    'mode': 'P'
}, {
    'sub': 'fixed/bordered.jpg',
    'convert': 'L',
    'mode': 'L'
}, {
    'sub': 'fixed/clear.jpg',
    'convert': 'L',
    'mode': 'L'
}, ))
def test_convert(path, image):
    with Img(fp=path(image['sub'])) as src, TemporaryFile() as tf:
        src.convert(image['convert'])
        src.save(fp=tf)
        with Img(fp=tf) as dest:
            assert (dest.width, dest.height, dest.mode, dest.frame_count) == (
                src.width, src.height, image['mode'], src.frame_count)
