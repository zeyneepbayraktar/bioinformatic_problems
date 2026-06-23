"""
Rosalind Problem 9: Finding a Motif in DNA
https://rosalind.info/problems/subs/

Given two DNA strings s and t, find all starting positions (1-indexed)
where t occurs as a substring of s.
"""

s = "GATATATGCATATACTT"
t = "ATAT"

sonuclar = []
for i in range(len(s)):
    if s[i:i + len(t)] == t:
        sonuclar.append(i + 1)

print(" ".join(map(str, sonuclar)))
