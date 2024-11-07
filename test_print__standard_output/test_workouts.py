import pytest

from workouts import print_workout_days


@pytest.mark.parametrize(
    "params",
    [
        ("upper body", "Mon, Thu\n"),
        ("lower body", "Tue, Fri\n"),
        ("30 min cardio", "Wed\n"),
        ("not a workout", "No matching workout\n"),
    ],
)
def test_print_workout_days(capsys, params):
    test_input, expected = params
    print_workout_days(test_input)
    out, err = capsys.readouterr()
    assert out == expected
