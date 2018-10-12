def read_file(file_name):
        text = ""
        try:
            file = open(file_name, "r")
            for line in file:
                text += line
        except:
            print("Something went wrong while reading file")
        finally:
            file.close()
        return text


def fasta_parser_rosalind(text):

        sequence_pieces = [x.strip() for x in text.split(">") if x.strip()]
        sequences = {}
        for piece in sequence_pieces:
            piece = piece.splitlines()
            name = piece[0].strip()
            seq = [x.strip() for x in piece[1:] if x.strip()]
            seq = "".join(seq)
            sequences[name] = seq
        return sequences


def count_cg_content(text):
        c_or_g = 0
        a_or_t = 0
        for x in range(0, len(text)):
            if text[x] == "C" or text[x] == "G":
                c_or_g += 1
            if text[x] == "A" or text[x] == "T":
                a_or_t += 1
        return c_or_g / (a_or_t + c_or_g) * 100

