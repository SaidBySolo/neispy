import pytest

from neispy import Neispy


@pytest.fixture
def client():
    yield Neispy.sync()
