DNA2MrNA = {
    'A': 'U',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

codonTable = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UGU': 'Cys', 'UGC': 'Cys',
    'UGG': 'Trp', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu',
    'CUG': 'Leu', 'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro',
    'CCG': 'Pro', 'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln',
    'CAG': 'Gln', 'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg',
    'CGG': 'Arg', 'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
    'AUG': 'Met', 'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr',
    'ACG': 'Thr', 'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys',
    'AAG': 'Lys', 'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg',
    'AGG': 'Arg', 'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val',
    'GUG': 'Val', 'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala',
    'GCG': 'Ala', 'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu',
    'GAG': 'Glu', 'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly',
    'GGG': 'Gly'
}

def findComplement(dna_sequence):
    complement = ""
    for nucleotide in dna_sequence:
        if nucleotide in DNA2MrNA:
            complement += DNA2MrNA[nucleotide]
        else:
            return None 
    return complement

def mRNA2protein(mRNA_sequence):
    amino_acids = []
    for i in range(0, len(mRNA_sequence), 3):
        codon = mRNA_sequence[i:i + 3]
        if codon in codonTable:
            amino_acids.append(codonTable[codon])
        else:
            amino_acids.append("Unknown") 
    return amino_acids


while True:
    dnaInput = input("Enter the DNA sequence: ").upper()

    # validate input
    if all(nucleotide in 'ATCG' for nucleotide in dnaInput):
        mRNAInput = findComplement(dnaInput)
        if mRNAInput is not None:
            print("mRNA Sequence:", mRNAInput)

            protein_sequence = mRNA2protein(mRNAInput)
            print("Amino Acid Sequence:", " - ".join(protein_sequence))
            break 
        else:
            print("Invalid DNA sequence.")
    else:
        print("Invalid input! Please enter a DNA sequence containing only A, T, C, and G.")