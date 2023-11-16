# phylorep
Simple script retrieving the ID of the best representative member of a gene/protein family, using the family phylogenetic tree as an input.

### Why?
This script was initially written to annotate protein/gene families (orthogroups) defined through orthology prediction (e.g. with [OrthoFinder](https://github.com/davidemms/OrthoFinder)).
Such families can include numerous members with different functional annotations. In large-scale comparative genomics, it may be convenient to consider a single protein annotation per orthogroup.
We suggest picking the best representative member of an orthogroup based on sequence similarity, more specifically using intra-orthogroup phylogenetic distances.

### How does it work?
The input phylogenetic tree is converted to a distance matrix, in which distances values correspond to the sum of branch lengths separating two tips.
The best representative member of the family is then defined as the most closely related protein/gene to all the other member of the family.
In practice, phylorep returns the tip separated from the other tree tips by the smallest phylogenetic distance.

### Requirements
phylorep is a Python3 script and requires the Python libraries [pandas](https://pandas.pydata.org/) and [biopython](https://biopython.org/) to be installed.
The libraries [sys](https://docs.python.org/3/library/sys.html), [argparse](https://docs.python.org/3/library/argparse.html) and [itertools](https://docs.python.org/3/library/itertools.html) (included in most Python distributions) must also be installed.

### Example run
```
python phyloRep.py -i geneFamilyTree.nwk
```
The input phylogenetic tree must be in the newick format.
