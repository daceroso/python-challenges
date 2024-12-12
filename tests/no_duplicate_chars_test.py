import pytest

from challenge_string.excercises.no_duplicate_chars import check_no_duplicate_chars


@pytest.mark.parametrize("value, expected", [
    ("Otto", False),
    ("Adrian", False),
    ("Micha", True),
    ("ABCDEFG", True)
])
def test_no_duplicate_chars(value, expected):
    assert check_no_duplicate_chars(value) == expected
