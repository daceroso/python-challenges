def dna_sequence(sequence):
    fraction = (sequence.count('G') + sequence.count('C')) / len(sequence)
    return fraction
