import utils_rosalind


def profile_matrix_2(dict_dna):
    dna_length = 0
    for v in dict_dna.values():
        dna_length = len(v)
        break
    list_a = [0 for i in range(dna_length)]
    list_c = [0 for i in range(dna_length)]
    list_g = [0 for i in range(dna_length)]
    list_t = [0 for i in range(dna_length)]
    print((len(list_t)))
    for string in dict_dna.values():
        for i in range(len(string)):
            if string[i] == "A":
                list_a[i] += 1
            if string[i] == "C":
                list_c[i] += 1
            if string[i] == "G":
                list_g[i] += 1
            if string[i] == "T":
                list_t[i] += 1
    return list_a, list_c, list_g, list_t


def consensus_string(dna_matrix):
    return 0


dict = utils_rosalind.fasta_parser_rosalind(utils_rosalind.read_file("C:\\Users\\Araragi\\Desktop\\rosalind.txt"))


profile_matr = profile_matrix_2(dict)
print(profile_matr[0])
print(profile_matr[1])
print(profile_matr[2])
print(profile_matr[3])
