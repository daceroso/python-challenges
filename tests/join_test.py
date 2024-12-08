import pytest

from challenge_string.excercises.joiner import join, join_with_reduce


@pytest.mark.parametrize("values, delimiter, expected",
                         [(["hello", "world", "message"], " +++ ",
                           "hello +++ world +++ message"),
                          (["Micha", "Germany"], " likes ",
                           "Micha likes Germany")])
def test_join(values, delimiter, expected):
    assert join(values, delimiter) == expected


@pytest.mark.parametrize("values, delimiter, expected",
                         [(["hello", "world", "message"], " +++ ",
                           "hello +++ world +++ message"),
                          (["Micha", "Germany"], " likes ",
                           "Micha likes Germany")])
def test_join(values, delimiter, expected):
    assert join_with_reduce(values, delimiter) == expected
