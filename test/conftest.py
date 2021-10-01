from neispy import Neispy
import pytest


@pytest.fixture
def client():
    yield Neispy.sync()
