from tempfile import TemporaryFile

import pytest
from PIL import ImageFilter

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'mode': 'RGBA',
}, {
    'sub': 'anima/clear.gif',
    'mode': 'RGBA',
}, {
    'sub': 'fixed/bordered.jpg',
}, {
    'sub': 'fixed/clear.jpg',
}, ))
def test_filter(path, image):
    with Img(fp=path(image['sub'])) as src, TemporaryFile() as tf:
        if 'mode' in image:
            src.convert(image['mode'])

        src.filter(ImageFilter.BLUR)
        src.save(fp=tf)
        with Img(fp=tf) as dest:
            assert (dest.width, dest.height, dest.frame_count) == (
                src.width, src.height, src.frame_count)
