"""simple script to remove double words in text file"""

from pathlib import Path

from get_all_words_from_text.use_txt_file import read_words_file, write_list_and_replace


def main(path_to_file):
    # list of words from words_file
    durty_list = read_words_file(path_to_file)
    print(len(durty_list))

    # create set from list
    words_set = set(durty_list)
    print(len(words_set))

    cleared_words_list = [word for word in words_set if len(word) > 2]

    write_list_and_replace(cleared_words_list, path_to_file)

    # check result
    durty_list = read_words_file(path_to_file)
    print(len(durty_list))


if __name__ == '__main__':
    print(main(f'{Path().home()}/Documents/ANKI/TEXTS/easy_words.txt'))
