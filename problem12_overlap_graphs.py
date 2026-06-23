"""
Rosalind Problem 12: Overlap Graphs
https://rosalind.info/problems/grph/

Given a collection of DNA strings in FASTA format, build the overlap
graph O3: a directed edge exists from string s to string t if the
length-3 suffix of s matches the length-3 prefix of t (and s != t).

This is the foundational idea behind genome assembly: figuring out
how DNA fragments can be chained together based on overlapping ends.
"""

veri = """>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG"""

sequences = {}
mevcut_id = ""

for satir in veri.split("\n"):
    if satir.startswith(">"):
        mevcut_id = satir[1:]
        sequences[mevcut_id] = ""
    else:
        sequences[mevcut_id] += satir

k = 3

for id1, seq1 in sequences.items():
    for id2, seq2 in sequences.items():
        if id1 != id2:
            if seq1[-k:] == seq2[:k]:
                print(id1, id2)
