from collections import defaultdict
import pickle

class KmerSet(object):
    """Object class for handling extraction of kmers from sequence data. Extracts total kmer counts."""
    
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

            # Initialize a defaultdict to count kmers in the dataset
            kmer_dict = defaultdict(int)

            for s in sequences:
                for i in range(len(s)-k):
                    kmer_dict[s[i:i+k]] += 1

            # Store the kmer dictionary as an attribute of the KmerSet object instance
            self.kmer_dict = kmer_dict

        else:
            raise Exception('This KmerSet already contains a kmer_dict.')
    
    def from_fasta(self, filename, k):
        """Function for extracting kmer counts from fasta file.

        Parameters

        ----------

        filename: str
            name of fasta sequence file
        k: int
            k-mer length
        """
        
        if self.kmer_dict == None:
            kmer_dict = defaultdict(int)
            
            # Open the specified fasta file and iterate over lines
            with open(filename) as f:
                
                for line in f:
                    if line[0] == ">":
                        pass
                    else:
                        line=line.strip()

                        for i in range(len(line)-k):
                            kmer_dict[line[i:i+k]] += 1

                self.kmer_dict = kmer_dict

        else:
            raise Exception('This KmerSet already contains a kmer_dict.')


class KmerSetPartitioned(object):
    """Object class for handling extraction of kmers from sequence data. Extracts kmer counts per sequence."""
    
    def __init__(self):
        """Instantiate a KmerSet object."""
        
        self.kmer_dict = None
    
    def from_list(self, sequences, k):

        """Function to count kmers in a list of sequences. Partitions kmer counts by sequence. 

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
        """Function for extracting kmer counts from fasta file.

        Parameters

        ----------

        filename: str
            name of fasta sequence file
        k: int
            k-mer length
        """
        
        # Currently this is getting kmer counts per line, not per sequence. Need to fix! 
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
