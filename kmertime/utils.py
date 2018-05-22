import numpy as np

def generate_seqs(alphabet, num_seqs, length):
    """Function to generate sequences of given length from defined alphabet.

    Parameters

    ----------

    alphabet: list
        list of bases to use
    num_seqs: int
        number of sequences to generate
    length: int
        length of the sequences
    """

    sequences = []
    
    for i in range(num_seqs):
        sequence = np.random.choice(alphabet, length)
        sequence = ''.join(sequence)
        sequences.append(sequence)
        
    return sequences
