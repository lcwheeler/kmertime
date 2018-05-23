# kmertime

*Simple Python API for counting kmers in sequence data*

kmertime is a simple Python API for counting k-mers in sequence data. It is a pure Python implementation meant for small to moderately sized datasets. In it's current form it is neither the fastest nor the most memory efficient approach to the problem of kmer counting, but the API is user friendly. If you have a reasonably small dataset and want to count kmers in python (i.e. in a Jupyter notebook, inline with the rest of your analysis) kmertime will do the trick. Issues and pull requests welcome! 


Basic example:

```python
from kmertime import KmerSet
from kmertime.utils import generate_seqs

# Use the generate_seqs function to create a list of random sequences
seqs = generate_seqs(alphabet=["A", "C", "T", "G"], num_seqs=10000, length=10000)

# Generate a "test" KmerSet object and count kmers in the simulated sequence data
test = KmerSet()

# Count all 3-mers in the random dataset
test.from_list(seqs, 3)

print("The total number of kmers is " + str(len(test.kmer_dict))+"\n")
print(test.kmer_dict)
```

```
The total number of kmers is 64

defaultdict(<class 'int'>, {'CCC': 1562072, 'CCG': 1561532, 'CGG': 1558930, 'GGA': 1559334, 'GAC': 1562467, 'ACT': 1560813, 'CTG': 1562341, 'TGT': 1562303, 'GTA': 1561751, 'TAA': 1563214, 'AAA': 1562421, 'AAC': 1561086, 'ACA': 1561054, 'CAT': 1563466, 'ATA': 1563044, 'AAT': 1563553, 'ATG': 1559588, 'TGA': 1561204, 'GAG': 1561104, 'AGT': 1562882, 'GTG': 1562173, 'TGC': 1560648, 'GCC': 1560141, 'GGG': 1559382, 'AGC': 1560912, 'GCT': 1560566, 'CTT': 1559318, 'TTG': 1563026, 'TAG': 1563143, 'AGG': 1561527, 'GGC': 1562010, 'CCA': 1563380, 'CAA': 1562104, 'AAG': 1562532, 'GTC': 1563247, 'TCA': 1562237, 'CAC': 1562874, 'GCG': 1562270, 'CGT': 1563125, 'ATC': 1562776, 'TCC': 1562737, 'ACC': 1562929, 'CTA': 1562477, 'TAC': 1562176, 'TGG': 1562976, 'GGT': 1562071, 'GTT': 1563175, 'TTT': 1562158, 'TTA': 1562601, 'TTC': 1561666, 'TCG': 1560839, 'CGC': 1562960, 'CTC': 1560559, 'GAT': 1561887, 'TCT': 1562475, 'TAT': 1561332, 'CAG': 1561858, 'AGA': 1563297, 'ATT': 1564855, 'ACG': 1563801, 'CGA': 1563437, 'CCT': 1560834, 'GCA': 1563561, 'GAA': 1561789})
```

## Install

Clone this repository and install a development version using `pip`:
```
pip install -e .
```
