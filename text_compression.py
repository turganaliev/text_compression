def tokenize_text(text):
    words = text.split()
    tokens = []
    for word in words:
        word = word.strip('!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~')
        if word:
            tokens.append(word)
    return tokens


def compress(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()

    words = tokenize_text(text)
    word_codes = {}
    code = 0
    compressed_text = []

    for word in words:
        if word not in word_codes:
            word_codes[word] = code
            code += 1
        compressed_text.append(str(word_codes[word]))

    with open(output_file, 'w') as f:
        f.write(' '.join(compressed_text))

    return word_codes


def decompress(input_file, output_file, word_codes):
    code_to_word = {int(code): word for word, code in word_codes.items()}

    with open(input_file, 'r') as f:
        compressed_text = f.read().split()

    decompressed_text = ' '.join(code_to_word[int(code)] for code in compressed_text)

    with open(output_file, 'w') as f:
        f.write(decompressed_text)


def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                return False
    return True


# Example usage
input_file = 'input.txt'
compressed_file = 'output.sc'
decompressed_file = 'readable.txt'

word_codes = compress(input_file, compressed_file)

decompress(compressed_file, decompressed_file, word_codes)

result = compare_files(input_file, decompressed_file)
print("Files are identical: ", result)
