"""
Rosalind Problem 10: Consensus and Profile
https://rosalind.info/problems/cons/

Given a collection of DNA strings of equal length in FASTA format,
build a profile matrix (count of A/C/G/T at each position) and
derive the consensus string (the most common symbol at each position).
"""

veri = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT"""

sequences = {}
mevcut_id = ""

for satir in veri.split("\n"):
    if satir.startswith(">"):
        mevcut_id = satir[1:]
        sequences[mevcut_id] = ""
    else:
        sequences[mevcut_id] += satir

n = len(list(sequences.values())[0])
profil = {
    "A": [0] * n,
    "C": [0] * n,
    "G": [0] * n,
    "T": [0] * n,
}

for id_, seq in sequences.items():
    for i, harf in enumerate(seq):
        profil[harf][i] += 1

consensus = ""
for i in range(n):
    en_yuksek = max("ACGT", key=lambda harf: profil[harf][i])
    consensus += en_yuksek

print(consensus)
for harf in "ACGT":
    print(f"{harf}: {' '.join(map(str, profil[harf]))}")
