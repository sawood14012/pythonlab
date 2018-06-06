def status(inf):
    num_lines = 0
    num_words = 0
    num_chars = 0

    with open(inf,'r')as fo:
        for line in fo:
            num_lines += 1
            wordline = line.split()
            num_words += len(wordline)
            for word in wordline:
                num_chars += len(word)

    print("number of lines: ", num_lines)
    print("number of words: ", num_words)
    print("number of characters: ", num_chars)


status("meer.txt")


