import numpy as np


def extract_sign_changes(seq):
    signs = np.sign(seq)
    sign_changes = ((np.roll(signs, 1) - signs) != 0).astype(int)
    return sign_changes

def extract_rolling_frequency(seq, n=100):
    seq_len = len(seq)
    sign_changes = extract_sign_changes(seq)
    freq = np.cumsum(sign_changes)
    freq = freq - np.pad(freq, n, mode='constant')[:seq_len]
    return (freq / n)

def extract_rolling_variance(seq, n=100):
    seq_len = len(seq)
    vari = np.cumsum(abs(seq))
    vari = vari - np.pad(vari, n, mode='constant')[:seq_len]
    return vari
     
