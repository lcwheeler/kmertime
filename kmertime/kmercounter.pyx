from collections import defaultdict

def kmer_counter(sequences, int k):

    """Function to count kmers in a list of sequences.

    Parameters

    ----------

    sequences: list
        list of sequence strings
    k: int
        k-mer length
    """
    

    # Initialize a defaultdict to count kmers in the dataset
    kmer_dict = defaultdict(int)

    for s in sequences:
        for i in range(len(s)-k):
            kmer_dict[s[i:i+k]] += 1


    return kmer_dict
