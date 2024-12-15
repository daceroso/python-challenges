import pytest

from mathematical.exercises.number_as_text import number_as_text


@pytest.mark.parametrize("n, expected",
                         [(7, "SEVEN "),
                          (42, "FOUR TWO "),
                          (7271, "SEVEN TWO SEVEN ONE "),
                          (24680, "TWO FOUR SIX EIGHT ZERO "),
                          (13579, "ONE THREE FIVE SEVEN NINE ")])
def test_number_as_text(n, expected):
    assert number_as_text(n) == expected
