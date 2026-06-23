"""
Rosalind Problem 4: Rabbits and Recurrence Relations
https://rosalind.info/problems/fib/

Given n months and k offspring per litter, compute the total number
of rabbit pairs after n months, following a modified Fibonacci recurrence:
F(n) = F(n-1) + k * F(n-2)
"""

n = 30
k = 4
f1 = 1
f2 = 1

for i in range(n - 2):
    yeni = f2 + k * f1
    f1 = f2
    f2 = yeni

print(f2)
