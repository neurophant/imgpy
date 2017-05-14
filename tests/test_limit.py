import pytest

from imgpy import Img


@pytest.mark.parametrize('image', ({'sub': 'anima/bordered.gif', 'frames': 38}, {'sub': 'anima/clear.gif', 'frames': 12}))
@pytest.mark.parametrize('limit', (None, 5, 100))
@pytest.mark.parametrize('shuffle', (True, False))
def test_limit(path, image, limit, shuffle):
    with Img(fp=path(image['sub'])) as src:
        src.load(limit=limit, shuffle=shuffle)
        assert src.n_frames <= limit if limit else src.n_frames == image['frames']
