def hamming_distance(string_1, string_2):
    if len(string_1) != len(string_2):
        raise Exception("Strings are not of equal length")
    hamming = 0
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            hamming += 1
    return hamming


print(hamming_distance("CCAAAGCGAC", "CGGAGGATAACCTCTAACTCT"))