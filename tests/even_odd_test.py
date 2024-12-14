import pytest

from mathematical.exercises.even_or_odd import is_even, is_odd


@pytest.mark.parametrize("n, expected",
                         [(1, False), (2, True),
                          (3, False), (4, True)])
def test_is_even(n, expected):
    assert is_even(n) == expected


@pytest.mark.parametrize("n, expected",
                         [(1, True), (2, False),
                          (3, True), (4, False)])
def test_is_odd(n, expected):
    assert is_odd(n) == expected
