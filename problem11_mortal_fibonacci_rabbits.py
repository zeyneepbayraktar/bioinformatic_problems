"""
Rosalind Problem 11: Mortal Fibonacci Rabbits
https://rosalind.info/problems/fibd/

Given n months and a lifespan of m months, compute the total number
of rabbit pairs remaining after n months, where each pair dies after
living exactly m months.

State is tracked as a list of age-group counts, where index 0 holds
the count of rabbits that are 1 month old.
"""

n, m = 86, 16
yaslar = [1] + [0] * (m - 1)  # age groups 1..m, starting with one newborn pair

for ay in range(2, n + 1):
    yeni_dogan = sum(yaslar[1:])  # pairs aged 2+ months can reproduce
    yaslar = [yeni_dogan] + yaslar[:-1]  # age everyone by one month; oldest group dies off

print("Toplam:", sum(yaslar))
