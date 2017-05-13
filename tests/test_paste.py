from tempfile import TemporaryFile

import pytest
from PIL import ImageFilter

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'box': (80, 40, 180, 140),
    'res': (480, 265, 38)
}, {
    'sub': 'anima/clear.gif',
    'box': (100, 50, 150, 100),
    'res': (500, 265, 12)
}, {
    'sub': 'fixed/bordered.jpg',
    'box': (25, 25, 50, 50),
    'res': (250, 250, 1)
}, {
    'sub': 'fixed/clear.jpg',
    'box': (5, 25, 55, 75),
    'res': (510, 350, 1)
}, ))
def test_paste(path, image):
    with Img(fp=path(image['sub'])) as src:
        src.paste(255, box=image['box'])
        with TemporaryFile() as tf:
            src.save(fp=tf)
            tf.seek(0)
            with Img(fp=tf) as dest:
                res = (dest.width, dest.height, dest.n_frames)
    assert res == image['res']
