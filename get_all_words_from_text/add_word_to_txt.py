from pathlib import Path


def create_file_if_no(path_to_txt):
    Path(path_to_txt).touch(exist_ok=True)


def add_word_to_txt(input_data: str, path_to_txt: str):
    create_file_if_no(path_to_txt)
    with open(path_to_txt, 'a') as text_file:
        text_file.write(f'{input_data}\n')


if __name__ == '__main__':
    add_word_to_txt("slonff", 'test.txt')
