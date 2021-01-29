#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Extract the longest transcript from the Trinity assembly sequence
# Usage： python get_longest_from_trinity.py Trinity.fasta


import sys
import os

file = sys.argv[1]
path = os.path.abspath(file)
name =  path.replace(path.split("/")[-1], path.split("/")[-1].split('.')[0] + '.longest.fa')

print(f"Starting {name} \n")


re = {}  
with open (path) as f:
    for line in f:
        seq = []
        if line.startswith('>'):
            id = line.split(' ')[0].split('_')  
            id = '_'.join(id[:4])  
        else:
            seq.append(line)

        if id not in re:
            re[id] = seq
        else:
            re[id] += seq

maxseq = {}
for k,v in re.items():
    seq = max(v, key=len)
    maxseq[k] = seq

with open(name,'w') as f:
    for k,v in maxseq.items():
        f.write( k +'\n')
        tem = v.__str__()
        f.write(tem)

print(f"Done of {name}  \n")
