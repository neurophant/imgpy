from tempfile import TemporaryFile

from PIL import Image
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
def test_transform(path, image):
    with Img(fp=path(image['sub'])) as src, TemporaryFile() as tf:
        src.transform(image['size'], Image.EXTENT, (0, 0) + image['size'])
        src.save(fp=tf)
        with Img(fp=tf) as dest:
            assert (dest.width, dest.height, dest.n_frames) == image['size'] + (src.n_frames, )
