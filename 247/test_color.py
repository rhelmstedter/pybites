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
        assert len(actual) == 7


def test_gen_hex_color_white(gen):
    with patch('color.sample') as mocked_sample:
        mocked_sample.return_value = [255, 255, 255]
        actual = next(gen)
        assert actual == "#FFFFFF"
        assert len(actual) == 7


def test_gen_hex_color_mid(gen):
    with patch('color.sample') as mocked_sample:
        mocked_sample.return_value = [100, 88, 159]
        actual = next(gen)
        assert actual == "#64589F"
        assert len(actual) == 7


def test_gen_hex_color_bad_sample(gen):
    with patch('color.sample') as mocked_sample:
        with pytest.raises(ValueError):
            mocked_sample.return_value = [100, 88, 159, 34]
            actual = next(gen)
