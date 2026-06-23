# Bioinformatic Problems

Bu repo, [Rosalind.info](https://rosalind.info) platformundaki biyoinformatik problemlerine ait çözümlerimi içerir. Bioinformatics alanına Bilgisayar Bilimleri öğrencisi olarak giriş yaparken adım adım öğrenme sürecimin bir parçasıdır.

## İçerik

| # | Problem | Konu |
|---|---------|------|
| 1 | [Counting DNA Nucleotides](problem01_counting_dna_nucleotides.py) | String işleme |
| 2 | [Transcribing DNA into RNA](problem02_transcribing_dna_to_rna.py) | String işleme |
| 3 | [Complementing a Strand of DNA](problem03_reverse_complement.py) | String işleme, `str.maketrans` |
| 4 | [Rabbits and Recurrence Relations](problem04_fibonacci_rabbits.py) | Dinamik programlama |
| 5 | [Computing GC Content](problem05_gc_content.py) | FASTA parsing |
| 6 | [Counting Point Mutations](problem06_hamming_distance.py) | Hamming distance |
| 7 | [Mendel's First Law](problem07_mendels_first_law.py) | Olasılık |
| 8 | [Translating RNA into Protein](problem08_translating_rna_to_protein.py) | BioPython, codon table |
| 9 | [Finding a Motif in DNA](problem09_finding_a_motif_in_dna.py) | Substring arama |
| 10 | [Consensus and Profile](problem10_consensus_and_profile.py) | FASTA parsing, profile matrix |
| 11 | [Mortal Fibonacci Rabbits](problem11_mortal_fibonacci_rabbits.py) | Dinamik programlama, state tracking |
| 12 | [Overlap Graphs](problem12_overlap_graphs.py) | Graf teorisi |
| 13 | [Calculating Expected Offspring](problem13_calculating_expected_offspring.py) | Beklenen değer |
| 14 | [Finding a Shared Motif](problem14_longest_common_substring.py) | Longest common substring |
| 15 | [Independent Alleles](problem15_independent_alleles.py) | Binom dağılımı, `scipy.stats` |

## Kullanılan Araçlar

- Python 3
- [BioPython](https://biopython.org/) — sequence/codon işlemleri için
- [SciPy](https://scipy.org/) — olasılık dağılımları için

## Kurulum

```bash
pip install biopython scipy
```

## Çalıştırma

Her dosya bağımsız olarak çalıştırılabilir:

```bash
python3 problem01_counting_dna_nucleotides.py
```

## Hakkında

Dokuz Eylül Üniversitesi Bilgisayar Bilimleri öğrencisiyim ve biyoinformatik?hesaplamalı biyoloji alanında kariyer yapmayı hedefliyorum. Bu repo, gerçek genomik veri üzerinde çalışmaya geçmeden önce temel algoritmik ve biyolojik kavramları pekiştirmek için attığım ilk adımları içeriyor.


