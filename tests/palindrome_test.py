import pytest

from challenge_string.exercises.palindrome import is_palindrome, is_palindrome_simple, is_palindrome_reverse


def palindrome_inputs_and_expecteds():
    return [("Otto", True),
            ("ABCBX", False),
            ("ABCXcba", True)]


@pytest.mark.parametrize("input, expected",
                         palindrome_inputs_and_expecteds())
def test_is_palindrome(input, expected):
    assert is_palindrome(input) == expected

@pytest.mark.parametrize("input, expected",
                         palindrome_inputs_and_expecteds())
def test_is_palindrome(input, expected):
    assert is_palindrome_simple(input) == expected

@pytest.mark.parametrize("input, expected",
                         palindrome_inputs_and_expecteds())
def test_is_palindrome(input, expected):
    assert is_palindrome_reverse(input) == expected
