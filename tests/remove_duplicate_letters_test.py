import pytest

from challenge_string.excercises.remove_duplicate_letters import remove_duplicates


@pytest.mark.parametrize("value, expected", [
    ("bananas", "bans"),
    ("lalalamama", "lam"),
    ("MICHAEL", "MICHAEL"),
    ("AaBbcCdD", "ABcd")
])
def test_remove_duplicate_letters(value, expected):
    assert remove_duplicates(value) == expected


