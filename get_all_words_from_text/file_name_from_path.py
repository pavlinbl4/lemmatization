from pathlib import Path


def file_name_with_ext(path_to_file: str):
    return Path(path_to_file).name


def file_name_no_ext(path_to_file: str):
    return Path(path_to_file).name.split('.')[0]


if __name__ == '__main__':
    path_to_book_file = '/Volumes/big4photo/Downloads/Lamb to the Slaughter.txt'
    assert type(file_name_with_ext(path_to_book_file)) == str
    assert file_name_with_ext(path_to_book_file) == 'Lamb to the Slaughter.txt'
    print(file_name_no_ext(path_to_book_file))
