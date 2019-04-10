from numpy.random import randint


def random_sub_sequence_indexes(full_sequence, seq_length, n=1):
    max_a = len(full_sequence) - seq_length
    start_indexes = [randint(max_a) for _ in range(n)]
    return [slice(start_i, start_i + seq_length) for start_i in start_indexes]

def subsequence_to_sample(subsequence):
    return subsequence['acoustic_data'].values, subsequence['time_to_failure'].tail(1).values
