import pytest

from challenge_string.exercises.dna_sequence import dna_sequence


@pytest.mark.parametrize("value, expected",
                         [("GATTACCTGAGCCTAC", 0.5)])
def test_dna_sequence(value, expected):
    assert dna_sequence(value) == expected