"""
Rosalind Problem 15: Independent Alleles
https://rosalind.info/problems/lia/

Starting from an AaBb organism (Tom), each generation mates with an
AaBb partner. Compute the probability that at least N organisms in
the k-th generation have genotype AaBb.

Each offspring is independently AaBb with probability 1/4 (1/2 for Aa
times 1/2 for Bb). The k-th generation has 2^k individuals, so this
becomes a binomial probability question.
"""

from scipy.stats import binom

k, N = 7, 37
n = 2 ** k
p = 0.25

# P(at least N) = 1 - P(fewer than N)
ihtimal = 1 - binom.cdf(N - 1, n, p)
print(ihtimal)
