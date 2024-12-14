import pytest

from challenge_string.exercises.reverse_string import reverse_string


@pytest.mark.parametrize("value, expected", [
    ("ABCD", "DCBA"),
    ("OTTO", "OTTO"),
    ("PETER", "RETEP"),
])
def test_reverse_string(value, expected):
    assert reverse_string(value) == expected
