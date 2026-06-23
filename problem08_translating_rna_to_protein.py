"""
Rosalind Problem 8: Translating RNA into Protein
https://rosalind.info/problems/prot/

Given an mRNA string, translate it into the corresponding protein
string by reading codons (3-letter groups) and converting each to
an amino acid, stopping at the first STOP codon.
"""

from Bio.Data import CodonTable

rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

tablo = CodonTable.unambiguous_rna_by_name["Standard"]

protein = ""
for i in range(0, len(rna), 3):
    codon = rna[i:i + 3]
    if codon in tablo.stop_codons:
        break
    protein += tablo.forward_table[codon]

print(protein)
