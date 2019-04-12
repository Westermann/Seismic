from numpy.random import choice, randint


def random_sub_sequence_indexes(full_sequence, seq_length, n=1):
    full_len = len(full_sequence)
    left_over = full_len % seq_length
    num_subseqs = full_len // seq_length
    start_index = randint(left_over)
    all_subseqs = [
        slice(start_i, start_i + seq_length) for start_i in
        range(start_index, full_len, seq_length)
    ]
    return choice(all_subseqs, n, replace=False)

def subsequence_to_sample(subsequence):
    return subsequence['acoustic_data'].values, subsequence['time_to_failure'].tail(1).values[0]
