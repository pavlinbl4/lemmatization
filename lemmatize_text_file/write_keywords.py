import os


def write_keywords_from_list(keywords: list, file_path: str):
    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(file_path, 'a') as text_file:
        for k_word in keywords:
            text_file.write(k_word + '\n')
