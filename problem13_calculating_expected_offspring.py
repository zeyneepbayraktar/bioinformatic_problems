"""
Rosalind Problem 13: Calculating Expected Offspring
https://rosalind.info/problems/iev/

Given the number of couples for each of six genotype pairings, and
assuming each couple has exactly two offspring, compute the expected
number of offspring displaying the dominant phenotype.

Genotype order: AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
"""

veri = "18271 18422 16769 16217 17470 16344"
ciftler = list(map(int, veri.split()))
ihtimaller = [1, 1, 1, 0.75, 0.5, 0]  # probability offspring shows dominant phenotype

toplam = 0
for cift, ihtimal in zip(ciftler, ihtimaller):
    toplam += cift * 2 * ihtimal

print(toplam)
