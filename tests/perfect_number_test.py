import pytest

from mathematical.exercises.perfect_number import is_perfect_number_simple


@pytest.mark.parametrize("n, expected",
                         [(6, True),
                          (28, True),
                          (496, True),
                          (8128, True)])
def test_is_perfect_number(n, expected):
    assert is_perfect_number_simple(n) == expected
