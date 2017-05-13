from tempfile import TemporaryFile

import pytest

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'angle': 90
}, {
    'sub': 'anima/clear.gif',
    'angle': 90
}, {
    'sub': 'fixed/bordered.jpg',
    'angle': 90
}, {
    'sub': 'fixed/clear.jpg',
    'angle': 90
}, ))
def test_rotate(path, image):
    with Img(fp=path(image['sub'])) as src, TemporaryFile() as tf:
        src.rotate(image['angle'], expand=True)
        src.save(fp=tf)
        with Img(fp=tf) as dest:
            assert (dest.width, dest.height) == (src.width, src.height)
