def reverse_string_dna(string):
    return string[::-1]


def complement_dna(pattern):
    s = ""
    for letter in pattern:
        if letter == "A":
            s += "T"
        elif letter == "T":
            s += "A"
        elif letter == "G":
            s += "C"
        elif letter == "C":
            s += "G"
        else:
            s += "?"
    return s

# return reversed complement DNA sequence


def reverse_complementary_dna(text):
    text = reverse_string_dna(text)
    text = complement_dna(text)
    return text

# return all positions of pattern in sequence


def pattern_matching(pattern, genome):
    positions = []
    k = len(pattern)
    for i in range(len(genome) - k + 1):
        if pattern == genome[i:i+k]:
            positions.append(i)

    return positions


def frequency_map(text, k):
    freq = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freq[pattern] = 0
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freq[pattern] += 1
    return freq


def frequent_words(text, k):
    words = []
    freq = frequency_map(text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words


def frequency_map(text, k):
    freq = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freq[pattern] = 0
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freq[pattern] +=1
    return freq


def acid_base_count(text):
    counter = {}
    counter["A"] = 0
    counter["T"] = 0
    counter["G"] = 0
    counter["C"] = 0
    for letter in text:
        if letter == "A":
            counter["A"] += 1
        elif letter == "T":
            counter["T"] += 1
        elif letter == "G":
            counter["G"] += 1
        elif letter == "C":
            counter["C"] += 1
        else:
            print("Not a DNA string")
    return counter


def transcribe_dna_to_rna(text):
    return text.replace("T", "U")








def fibonacci_rabbits(n, k):
    young = 0
    current = 1
    total = 1
    if n == 1:
        return 1
    else:
        for i in range(n-1):
            sum = current + young*k
            young = current
            current = sum
    return sum


def computing_gc_content(text):
    cg_len = 0
    for i in range(len(text)):
        if text[i] == "C" or text[i] == "G":
            cg_len += 1
    return cg_len / len(text)




print(computing_gc_content("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"))


# wat the fuk

