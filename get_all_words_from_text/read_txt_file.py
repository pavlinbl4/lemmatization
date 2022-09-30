def read_words_file(path_to_file):
    with open(path_to_file, 'r') as text_file:
        return text_file.read().splitlines()