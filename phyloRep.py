#!/bin/python
import argparse
import pandas as pd
import sys
from Bio import Phylo
from itertools import combinations_with_replacement 

def get_params(argv):
    parser = argparse.ArgumentParser(description='Analyses the distances in a phylogenetic tree to identify the best representative sequence')
    parser.add_argument('-i', '--input', help="Phylogenetic tree", required=True)
    a = parser.parse_args()
    return a

def getDistMatrix(tree):
    nodes=[a.name for a in tree.depths(unit_branch_lengths=True) if a.name!=None]
    comb=list(combinations_with_replacement(nodes, 2))
    df=pd.DataFrame(index=nodes, columns=nodes)
    for c in comb:
        df.loc[c[0],c[1]]=tree.distance(c[0],c[1])
        df.loc[c[1],c[0]]=df.loc[c[0],c[1]]
    return df

if __name__ == '__main__':
    a = get_params(sys.argv[1:])
    tree=Phylo.read(a.input, 'newick')
    distmat=getDistMatrix(tree)
    distmat['sum']=distmat.sum(axis=1)
    distmat=distmat.sort_values(by='sum',ascending=True)
    print(distmat.index[0])
