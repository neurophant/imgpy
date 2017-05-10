import os

import pytest


@pytest.fixture
def path():
    def func(sub):
        return os.path.join(os.path.dirname(__file__), sub)

    return func
