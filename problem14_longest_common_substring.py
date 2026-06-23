"""
Rosalind Problem 14: Finding a Shared Motif (Longest Common Substring)
https://rosalind.info/problems/lcsm/

Given a collection of DNA strings in FASTA format, find a longest
common substring shared by all of them. Multiple correct answers
may exist; any one of equal maximum length is accepted.

This mirrors a real bioinformatics task: finding shared DNA motifs
across multiple sequences (e.g. comparing related virus genomes).
"""

veri = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""

sequences = {}
mevcut_id = ""

for satir in veri.split("\n"):
    if satir.startswith(">"):
        mevcut_id = satir[1:]
        sequences[mevcut_id] = ""
    else:
        sequences[mevcut_id] += satir

tum_seqler = list(sequences.values())
en_kisa = min(tum_seqler, key=len)

en_uzun_ortak = ""
for baslangic in range(len(en_kisa)):
    for bitis in range(len(en_kisa), baslangic, -1):
        parca = en_kisa[baslangic:bitis]
        if len(parca) <= len(en_uzun_ortak):
            break
        if all(parca in seq for seq in tum_seqler):
            en_uzun_ortak = parca

print(en_uzun_ortak)
