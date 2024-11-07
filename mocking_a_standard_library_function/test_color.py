from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


@pytest.mark.parametrize(
    "mock_return, target_hex",
    [
        ([0, 0, 0], "#000000"),
        ([255, 255, 255], "#FFFFFF"),
    ],
)
def test_gen_hex_color(gen, mock_return, target_hex):
    with patch("color.sample", wraps=color.sample) as mocked_sample:
        mocked_sample.return_value = mock_return
        actual = next(gen)
        assert len(actual) == 7
        assert actual == target_hex
        mocked_sample.assert_called_once_with(range(0, 256), 3)


def test_gen_hex_color_bad_sample(gen):
    with patch("color.sample", wraps=color.sample) as mocked_sample:
        with pytest.raises(ValueError):
            mocked_sample.return_value = [100, 88, 159, 34]
            next(gen)
