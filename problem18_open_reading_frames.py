codon_table = {
    'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
    'TAT':'Y', 'TAC':'Y', 'TAA':'Stop', 'TAG':'Stop',
    'TGT':'C', 'TGC':'C', 'TGA':'Stop', 'TGG':'W',
    'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
    'ATT':'I', 'ATC':'I', 'ATA':'I', 'ATG':'M',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'AAT':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
    'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
}
def reverse_complement(dna):
    tablo = str.maketrans("ATGC", "TACG")
    komplement = dna.translate(tablo)
    return komplement[::-1]

def find_proteins(dna):
    proteins = set()
    for i in range(len(dna) - 2):
        if dna[i:i+3] == "ATG":
            protein = ""
            for j in range(i, len(dna) - 2, 3):
                codon = dna[j:j+3]
                amino_acid = codon_table.get(codon)
                if amino_acid == "Stop":
                    proteins.add(protein)
                    break
                elif amino_acid is None:
                    break
                else:
                    protein += amino_acid
    return proteins

dna = """TCCTACTTGAAGGAACACAGACTTGTACCTAAGTGTAACGTTGTACGCGAATGGTTGCGA
CGGGGATACAGAGCGCCGCTATAGCAGCATAGCGCTGATGCGCAAGAGATTCTAGCTTGG
TTGTCGACAATGTTCGCTCTTTTAAGTTTGAGCAGCCTTTAAGTATTCAGCCTCATGGGG
ACTAGCTGCTGCTAGCTTCAATTAAGTAGGCACTTTTGTCCAGCCCCAGATTAGATAGAT
CACCGTTCTGACGGGGGGCCCCCGCACGTAGTTATGAGGCCTACCTTGACCTATTACCTT
GTCAGGTCCCTCAGTAAGGGATACTTCGGGTCATTCGGAATGCCGGCGTGTAGGTAAGCT
AAGTCTTTAGTCAGGTGTCCAGAGGGTAGCGGGGTTCGATTGTACCAGACTTTATACGCA
GTGATGGCCTTTGTCAATTTCCGGAATATACGGTAGCTACCGTATATTCCGGAAATTGAC
AAAGGCCATTCACTCACTTGGTGCTGACTCGATCAGTGTTTCTGGCCACTCTCCGTCCGT
GTTGGCCCCACGCCGTTAACACGCAGGTTCCGGCTTTGTTCCGTGGTTTATCAAAGCGAA
TGGTAGGTCGTTTTCCTGAAGGCGTATGCAAGTCGGAATATGGCCGAGTCAGCGTGTGTC
AAAGAACTGTCTCCTGCCCTATTCTAGGACCAGTTTTTTTTTAATAATTCGAGTTAGTGG
GGACGCTTTCCAGCTGGCAGCACACGGATTTCTGAAAGACCGGGTCGTGCGCGGACTCAG
GCAGCCCTCTGCTGCGCACTTTGAATTTCAGGAAGCATTACAGTTCCCGTGGTTTCCCCG
GCCCAACTACTGTTCACAGGGCCGAGTATGAATCTCAATTGATACTAAATGTAGATAGCA
CTCAGTCGTGGA""".replace("\n", "")

all_proteins = find_proteins(dna) | find_proteins(reverse_complement(dna))

for protein in all_proteins:
    print(protein)