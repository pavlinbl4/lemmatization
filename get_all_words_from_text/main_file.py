"""
create text file with potential unknown words in book
"""

from tkinter import filedialog

from get_all_words_from_text.clear_list_of_words import remove_easy_words
from get_all_words_from_text.file_name_from_path import file_name_with_ext
from get_all_words_from_text.use_txt_file import read_words_file, add_word_to_txt, create_file_if_no, \
    write_list_and_replace
from lemmatize_book import lemma_word_from_text_file
from pathlib import Path
from icecream import ic


def create_words_to_learn_or_skip(book_title, path_to_book_file):
    # check existing of the file words_to_learn-book_title.txt
    # if no such file get lemma words from book if  words_to_learn-book_title.txt exist go to line
    path_to_words_file = f'{Path().home()}/Documents/ANKI/TEXTS/words_to_learn_file-{book_title}'
    if Path(path_to_words_file).exists():
        print("This book was processed later use words from file")
    else:
        lemma_words = lemma_word_from_text_file(path_to_book_file)  # get lemma words from book
        for word in lemma_words:
            add_word_to_txt(word, path_to_words_file)  # save this collection for future use
        print(f'file with word from {book_title} created')
    return path_to_words_file


def select_file():  # return path to the file
    return filedialog.askopenfilename(initialdir=f'{Path().home()}/Documents/ANKI/TEXTS', defaultextension='txt')


def main():
    # select text file from gui
    # path_to_book_file = select_file()
    path_to_book_file = '/Users/evgenii/Documents/ANKI/TEXTS/Full Dark, No Stars - FAIR EXTENSION.txt'

    # get title of the book
    book_title = file_name_with_ext(path_to_book_file)
    print(f'{book_title = }')

    # make lemmatization from text or skip it
    path_to_words_file = create_words_to_learn_or_skip(book_title, path_to_book_file)

    # check existing of the file easy_words.txt and create it if NO
    create_file_if_no(f'{Path().home()}/Documents/ANKI/TEXTS/easy_words.txt')

    # all known words
    easy_word = read_words_file(f'{Path().home()}/Documents/ANKI/TEXTS/easy_words.txt')

    # number of easy words
    easy_word_count = len(easy_word)
    print(f'{easy_word_count = }')

    all_words = read_words_file(path_to_words_file)
    all_words_count = len(all_words)  # number words before optimization

    # remove easy words from file
    cleared_words = remove_easy_words(all_words, easy_word)

    # overwrite words_to_learn file with clear words
    write_list_and_replace(cleared_words,
                           path_to_words_file)
    print(f'easy words removed from words file, now there are {len(read_words_file(path_to_words_file))}  words')


if __name__ == '__main__':
    main()
