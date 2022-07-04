from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def test_gen_hex_color_black(gen):
    with patch('color.sample') as mocked_sample:
        mocked_sample.return_value = [0, 0, 0]
        actual = next(gen)
        assert actual == "#000000"


def test_gen_hex_color_white(gen):
    with patch('color.sample') as mocked_sample:
        mocked_sample.return_value = [255, 255, 255]
        actual = next(gen)
        assert actual == "#FFFFFF"


def test_gen_hex_color_mid(gen):
    with patch('color.sample') as mocked_sample:
        mocked_sample.return_value = [100, 88, 159]
        actual = next(gen)
        assert actual == "#64589F"
