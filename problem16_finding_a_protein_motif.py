"""
Rosalind Problem 16: Finding a Protein Motif
https://rosalind.info/problems/mprt/

Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif (N{P}[ST]{P}),
output its given access ID followed by a list of locations in the protein
string where the motif can be found.
"""

import requests

def find_motif(sequence):
    positions = []
    for i in range(len(sequence) - 3):
        window = sequence[i:i+4]
        if (window[0] == 'N' and window[1] != 'P' and window[2] in 'ST' and window[3] != 'P'):
            positions.append(i + 1)
    return positions

ids = ["P19823_ITH2_HUMAN", "O13188", "Q3BN23", "P03415_VME1_CVMA5",
       "P98119_URT1_DESRO", "Q7S432", "P06765_PLF4_RAT", "P11171_41_HUMAN",
       "P01190_COLI_BOVIN", "A1UR66", "P01866_GCB_MOUSE", "P0A4Y7",
       "P01046_KNL1_BOVIN"]

for uniprot_id in ids:
    clean_id = uniprot_id.split("_")[0]
    url = f"https://rest.uniprot.org/uniprotkb/{clean_id}.fasta"
    response = requests.get(url)

    lines = response.text.splitlines()
    sequence = ""
    for line in lines:
        if line.startswith(">"):
            continue
        sequence += line

    result = find_motif(sequence) 
    if result:  
        print(uniprot_id)
        print(" ".join(str(p) for p in result)) 
  
    
   