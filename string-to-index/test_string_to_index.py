import pytest

from string_to_index import convert_string_to_index


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        pytest.param("A", [0], id="Single letter A"),
        pytest.param("B", [1], id="Single letter B"),
        pytest.param("Z", [25], id="Single letter Z"),
        pytest.param(["A", "B", "Z"], [0, 1, 25], id="Single letters in list [A, B, Z]"),
        pytest.param("A, B, C", [0, 1, 2], id="Multiple single letters 'A, B, C'"),
        pytest.param("A:C", [0, 1, 2], id="Range A:C"),
        pytest.param("A:C, E:G", [0, 1, 2, 4, 5, 6], id="Multiple ranges A:C, E:G"),
        pytest.param("A:C, B:D",  [0, 1, 2, 1, 2, 3], id="Overlapping ranges A:C, B:D"),
        pytest.param("A:B, D:E", [0, 1, 3, 4], id="Non-continuous ranges A:B, D:E"),
        pytest.param(["A", "B:C", "D"], [0, 1, 2, 3], id="Mixed single letters and ranges [A, B:C, D]"),
        pytest.param(" A , B : C , D ", [0, 1, 2, 3], id="Handling whitespace in ' A , B : C , D '"),
        pytest.param("AA, AB, AC", [26, 27, 28], id="Longer letter range AA, AB, AC"),
        pytest.param("AA:AC", [26, 27, 28], id="Longer letter range with colon AA:AC"),
        pytest.param(["A", "C:D", "AA"], [0, 2, 3, 26], id="Mixed single, range, and longer letters [A, C:D, AA]"),
        pytest.param("", [], id="Empty string"),
        pytest.param([], [], id="Empty list")
    ]
)
def test_convert_string_to_index(input_value, expected_output):
    assert convert_string_to_index(input_value) == expected_output