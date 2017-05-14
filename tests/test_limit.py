import pytest

from imgpy import Img


@pytest.mark.parametrize('image', ({'sub': 'anima/bordered.gif', 'frames': 38}, {'sub': 'anima/clear.gif', 'frames': 12}))
@pytest.mark.parametrize('limit', (None, 5, 100))
@pytest.mark.parametrize('first', (True, False))
def test_limit(path, image, limit, first):
    with Img(fp=path(image['sub'])) as src:
        src.load(limit=limit, first=first)
        assert src.frame_count <= limit if limit else src.frame_count == image['frames']
