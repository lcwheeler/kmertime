from collections import defaultdict
import pickle

class KmerSet(object):
    """Object class for handling extraction of kmers from sequence data."""
    
    def __init__(self):
        """Instantiate a KmerSet object."""
        
        self.kmer_dict = None
    
    def from_list(self, sequences, k):

        """Function to count kmers in a list of sequences.

        Parameters

        ----------

        sequences: list
            list of sequence strings
        k: int
            k-mer length
        """

        if self.kmer_dict == None:

            kmer_dict = {}

            for s in sequences:
                d = defaultdict(int)
                
                for i in range(len(s)-k):
                    d[s[i:i+k]] += 1
                kmer_dict[s] = d

            self.kmer_dict = kmer_dict

        else:
            raise Exception('This KmerSet already contains a kmer_dict.')
    
    def from_fasta(self, filename, k):
        """Function for pulling sequences from fasta file.

        Parameters

        ----------

        filename: str
            name of fasta sequence file
        k: int
            k-mer length
        """
        
        if self.kmer_dict == None:
            kmer_dict = {}
            
            with open(filename) as f:
                
                for line in f:
                    if line[0] == ">":
                        pass
                    else:
                        line=line.strip()
                        d = defaultdict(int)

                        for i in range(len(line)-k):
                            d[line[i:i+k]] += 1
                        kmer_dict[line] = d

                self.kmer_dict = kmer_dict

        else:
            raise Exception('This KmerSet already contains a kmer_dict.')


