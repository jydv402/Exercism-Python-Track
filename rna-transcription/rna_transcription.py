def to_rna(dna_strand):
    rna = ""
    for tide in dna_strand:
        if tide == "G":
            rna += "C"
        elif tide == "C":
            rna += "G"
        elif tide == "T":
            rna += "A"
        elif tide == "A":
            rna += "U"
    return rna
