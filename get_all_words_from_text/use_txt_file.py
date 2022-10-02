from pathlib import Path


def read_words_file(path_to_file: str) -> list:
    with open(path_to_file, 'r') as text_file:
        return text_file.read().splitlines()


def create_file_if_no(path_to_txt):
    Path(path_to_txt).touch(exist_ok=True)


def add_word_to_txt(input_data, path_to_txt: str):
    create_file_if_no(path_to_txt)
    with open(path_to_txt, 'a') as text_file:
        text_file.write(f'{input_data}\n')

def write_list_and_replace(input_list:list, path_to_txt):
    with open(path_to_txt,'w') as over_writen_txt:
        for _ in input_list:
            over_writen_txt.write(f'{_.strip()}\n')


if __name__ == '__main__':
    list_from_txt = read_words_file('easy_words copy.txt')
    write_list_and_replace(list_from_txt,'easy_words copy_to_delete.txt')

