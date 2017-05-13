from tempfile import TemporaryFile

import pytest
from PIL import ImageFilter

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'mode': 'RGBA',
    'res': 38
}, {
    'sub': 'anima/clear.gif',
    'mode': 'RGBA',
    'res': 12
}, {
    'sub': 'fixed/bordered.jpg',
    'res': 1
}, {
    'sub': 'fixed/clear.jpg',
    'res': 1
}, ))
def test_filter(path, image):
    with Img(fp=path(image['sub'])) as src:
        if 'mode' in image:
            src.convert(image['mode'])

        src.filter(ImageFilter.BLUR)
        with TemporaryFile() as tf:
            src.save(fp=tf)
            tf.seek(0)
            with Img(fp=tf) as dest:
                res = dest.n_frames
    assert res == image['res']
