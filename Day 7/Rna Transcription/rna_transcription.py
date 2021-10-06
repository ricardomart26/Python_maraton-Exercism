def to_rna(dna_strand):
    rna_strand = ""
    for i in dna_strand:
        if i is 'A':
            rna_strand += 'U'
        elif i is 'C':
            rna_strand += 'G'
        elif i is 'G':
            rna_strand += 'C'
        elif i is 'T':
            rna_strand += 'A'
    return rna_strand
