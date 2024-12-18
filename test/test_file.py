import pytest


@pytest.fixture()
def before_after():
    print("Before test")
    yield
    print("\nAfter test")


def test_number_1():
    assert 1 == 1


def test_number_2(before_after):
    assert 2 == 3
