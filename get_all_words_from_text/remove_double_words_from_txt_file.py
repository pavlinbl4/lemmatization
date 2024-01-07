"""simple script to remove double words in text file"""

from pathlib import Path
from get_all_words_from_text.use_txt_file import read_words_file, write_list_and_replace


def main_remove_doubles_words_in_txt_file(path_to_file):
    # list of words from words_file
    durty_list = read_words_file(path_to_file)
    print(f'words before optimisation - {len(durty_list)}')

    # create set from list
    words_set = set(durty_list)
    print(f"words after optimisation - {len(words_set)}")

    cleared_words_list = [word.strip() for word in words_set if len(word) > 2]

    write_list_and_replace(cleared_words_list, path_to_file)


if __name__ == '__main__':
    main_remove_doubles_words_in_txt_file(f'{Path().home()}/Documents/ANKI/TEXTS/easy_words.txt')
