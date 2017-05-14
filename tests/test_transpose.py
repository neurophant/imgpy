from tempfile import TemporaryFile

from PIL import Image
import pytest

from imgpy import Img


@pytest.mark.parametrize('image', ('anima/bordered.gif', 'anima/clear.gif',
                                   'fixed/bordered.jpg', 'fixed/clear.jpg'))
def test_transpose(path, image):
    with Img(fp=path(image)) as src, TemporaryFile() as tf:
        src.transpose(Image.FLIP_LEFT_RIGHT)
        src.save(fp=tf)
        with Img(fp=tf) as dest:
            assert (dest.width, dest.height,
                    dest.frame_count) == (src.width, src.height, src.frame_count)
