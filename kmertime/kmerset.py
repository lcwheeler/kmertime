from .kmercounter import kmer_counter
from Bio import SeqIO
from collections import defaultdict

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

            # Use the cython kmercounter module to count kmers and store dictionary as attribute
            self.kmer_dict = kmer_counter(sequences, k)

        else:
            raise Exception('This KmerSet already contains a kmer_dict!')

    
    def from_fasta(self, filename, k, memory=True):
        """Function for extracting kmer counts from fasta file.

        Parameters

        ----------

        filename: str
            name of fasta sequence file
        k: int
            k-mer length
        memory: bool
            indicate whether to conserve memory
        """
        
        #if self.kmer_dict == None:
            #kmer_dict = defaultdict(int)
            
            # Open the specified fasta file and iterate over lines
            #with open(filename) as f:
                
                #for line in f:
                    #if line[0] == ">":
                        #pass
                    #else:
                        #line=line.strip()

                        #for i in range(len(line)-k):
                            #kmer_dict[line[i:i+k]] += 1

                #self.kmer_dict = kmer_dict

        #else:
            #raise Exception('This KmerSet already contains a kmer_dict!')

        if memory == True:

            if self.kmer_dict == None:
                kmer_dict = defaultdict(int)
                
                # Open the specified fasta file and iterate over fasta seqs using biopython
                with open(filename, 'r') as f:
                    
                    for record in SeqIO.parse(f, "fasta"):
                        seq = str(record.seq)

                        for i in range(len(seq)-k):
                            kmer_dict[seq[i:i+k]] += 1

                self.kmer_dict = kmer_dict

            else:
                raise Exception('This KmerSet already contains a kmer_dict!')

        else:

            if self.kmer_dict == None:
                kmer_dict = defaultdict(int)


                # Open the specified fasta file, pull seqs as a list, iterate over seqs
                records = list(SeqIO.parse("example.fasta", "fasta"))

                for i in range(len(records)):
                    seq = str(records[i].seq)

                    for i in range(len(seq)-k):
                        kmer_dict[seq[i:i+k]] += 1

                self.kmer_dict = kmer_dict

            else:
                raise Exception('This KmerSet already contains a kmer_dict!')
                
  


            

