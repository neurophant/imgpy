import pytest

from imgpy import Img


@pytest.mark.parametrize('image', ({
    'sub': 'exif/copyright.jpeg'
}, {
    'sub': 'exif/gps.jpg'
}))
def test_convert(path, image):
    with Img(fp=path(image['sub'])) as src:
        pass
