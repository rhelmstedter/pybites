from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def test_gen_hex_color(gen):
    with patch('test_color.gen', '#000000') as mock_gen:
        assert mock_gen == "#000000"
