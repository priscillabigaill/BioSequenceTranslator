aminoAcid2Codon = {
    'Phe': ['UUU', 'UUC'], 'Leu': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'Ser': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'Tyr': ['UAU', 'UAC'],
    'Cys': ['UGU', 'UGC'], 'Trp': ['UGG'], 'Pro': ['CCU', 'CCC', 'CCA', 'CCG'],
    'His': ['CAU', 'CAC'], 'Gln': ['CAA', 'CAG'], 'Arg': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Ile': ['AUU', 'AUC', 'AUA'], 'Met': ['AUG'], 'Thr': ['ACU', 'ACC', 'ACA', 'ACG'],
    'Asn': ['AAU', 'AAC'], 'Lys': ['AAA', 'AAG'], 'Val': ['GUU', 'GUC', 'GUA', 'GUG'],
    'Ala': ['GCU', 'GCC', 'GCA', 'GCG'], 'Asp': ['GAU', 'GAC'], 'Glu': ['GAA', 'GAG'],
    'Gly': ['GGU', 'GGC', 'GGA', 'GGG']
}

aminoAcidDict = {
    'F': 'Phe', 'L': 'Leu', 'S': 'Ser', 'Y': 'Tyr', 'C': 'Cys', 'W': 'Trp', 'P': 'Pro',
    'H': 'His', 'Q': 'Gln', 'R': 'Arg', 'I': 'Ile', 'M': 'Met', 'T': 'Thr', 'N': 'Asn',
    'K': 'Lys', 'V': 'Val', 'A': 'Ala', 'D': 'Asp', 'E': 'Glu', 'G': 'Gly'
}

while True:
    aminoAcidInput = input("Enter the amino acid sequence").upper()
    if all(aa in aminoAcidDict for aa in aminoAcidInput):
        break 
    else:
        print("Invalid amino acid code(s) detected. Please enter valid codes.")

possibleCodons = []

for aa in aminoAcidInput:
    fullName = aminoAcidDict.get(aa)
    if fullName:
        codons = aminoAcid2Codon.get(fullName, [])
        possibleCodons.append(codons)
    else:
        print(f"Invalid amino acid code: {aa}")

for i, codons in enumerate(possibleCodons):
    print(f"Amino Acid {aminoAcidInput[i]} (Full Name: {aminoAcidDict[aminoAcidInput[i]]}):")
    print(f"Possible Codons: {', '.join(codons)}")

while True:
    mRNASeq = input("Enter the mRNA sequence: ").upper()
    if all(nucleotide in 'AUCG' for nucleotide in mRNASeq):
        break  
    else:
        print("Invalid mRNA sequence. Please enter a sequence containing only A, U, C, and G.")

codonCount = {}
for codons in possibleCodons:
    for codon in codons:
        codonCount[codon] = mRNASeq.count(codon)

print("\nCodon Frequencies in the mRNA sequence:")
for codon, count in codonCount.items():
    print(f"{codon}: {count}")
