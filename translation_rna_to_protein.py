def translate_rna_to_prot(rna):
    protein = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]
        aminoacid = codon_to_protein(codon)
        if aminoacid == "stop":
            return protein
        else:
            protein += aminoacid
    return protein


def codon_to_protein(text):
    if len(text) != 3:
        raise Exception("{} doesn't look like a codon".format(text))
    if text == "UUU" or text == "UUC":
        return "F"
    if text == "UUA" or text == "UUG":
        return "L"
    if text == "UCU" or text == "UCC" or text == "UCA" or text == "UCG":
        return "S"
    if text == "UAU" or text == "UAC":
        return "Y"
    if text == "UAA" or text == "UAG" or text == "UGA":
        return "stop"
    if text == "UGU" or text == "UGC":
        return "C"
    if text == "UGG":
        return "W"
    if text == "CUU" or text == "CUC" or text == "CUA" or text == "CUG":
        return "L"
    if text == "CCU" or text == "CCC" or text == "CCA" or text == "CCG":
        return "P"
    if text == "CAU" or text == "CAC":
        return "H"
    if text == "CAA" or text == "CAG":
        return "Q"
    if text == "CGU" or text == "CGC" or text == "CGA" or text == "CGG":
        return "R"
    if text == "AUU" or text == "AUC" or text == "AUA":
        return "I"
    if text == "AUG":
        return "M"
    if text == "ACU" or text == "ACC" or text == "ACG":
        return "T"
    if text == "AAU" or text == "AAC":
        return "N"
    if text == "AAA" or text == "AAG":
        return "K"
    if text == "AGU" or text == "AGC":
        return "S"
    if text == "AGA" or text == "AGG":
        return "R"
    if text == "GUU" or text == "GUC" or text == "GUA" or text == "GUG":
        return "V"
    if text == "GCU" or text == "GCC" or text == "GCA" or text == "GCG":
        return "A"
    if text == "GAU" or text == "GAC":
        return "D"
    if text == "GAA" or text == "GAG":
        return "E"
    if text == "GGU" or text == "GGC" or text == "GGA" or text == "GGG":
        return "G"
    else:
        return "{} - unknown codon".format(text)

result = translate_rna_to_prot("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")
print(result)