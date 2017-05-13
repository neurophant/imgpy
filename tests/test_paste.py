from tempfile import TemporaryFile

import pytest
from PIL import ImageFilter

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'anima/bordered.gif',
    'box': (80, 40, 180, 140),
}, {
    'sub': 'anima/clear.gif',
    'box': (100, 50, 150, 100),
}, {
    'sub': 'fixed/bordered.jpg',
    'box': (25, 25, 50, 50),
}, {
    'sub': 'fixed/clear.jpg',
    'box': (5, 25, 55, 75),
}, ))
def test_paste(path, image):
    with Img(fp=path(image['sub'])) as src, TemporaryFile() as tf:
        src.paste(255, box=image['box'])
        src.save(fp=tf)
        with Img(fp=tf) as dest:
            assert (dest.width, dest.height, dest.n_frames) == (src.width, src.height, src.n_frames)
