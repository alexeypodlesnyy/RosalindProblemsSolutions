import utils_rosalind

path_to_data = "C:\\Users\\Araragi\\Desktop\\rosalind.txt"


text = utils_rosalind.read_file(path_to_data)
sequenses = utils_rosalind.fasta_parser_rosalind(text)


def highest_gc_cont(seq_list):
    max_gc = 0
    max_gc_name = ""
    for name, seq in seq_list.items():
        print(name)
        print(seq)
        current_gc = utils_rosalind.count_cg_content(seq)
        if current_gc > max_gc:
            max_gc = current_gc
            max_gc_name = name

    return max_gc_name, max_gc

print(highest_gc_cont(sequenses))