"""
Rosalind Problem 7: Mendel's First Law
https://rosalind.info/problems/iprb/

Given a population of k homozygous dominant (AA), m heterozygous (Aa),
and n homozygous recessive (aa) organisms, compute the probability
that two randomly selected mating organisms produce an offspring
with the dominant phenotype.
"""

k, m, n = 27, 30, 18
toplam = k + m + n

ciftler = toplam * (toplam - 1) / 2

# Probability that offspring is fully recessive (aa), broken down by parent pairing:
#   aa x aa -> always aa
#   Aa x aa -> 50% aa
#   Aa x Aa -> 25% aa
aa_ihtimal = (n * (n - 1) / 2 * 1 + m * n * 0.5 + m * (m - 1) / 2 * 0.25) / ciftler

print(1 - aa_ihtimal)
