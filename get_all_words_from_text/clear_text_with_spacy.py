# https://spacy.io/usage
import os
import pyperclip
from colorama import Fore
from add_word_to_txt import add_word_to_txt
from pathlib import Path

from get_all_words_from_text.lemmatize_book import lemma_word_from_text_file
from use_txt_file import read_words_file


def read_easy_words_file(path_to_file):
    with open(path_to_file, 'r') as text_file:
        return text_file.read().splitlines()


def clear_words_collection(lemmatised_set: set) -> list:
    cleared_words = []
    easy_words = read_words_file(read_easy_words_file)
    for word in lemmatised_set:
        if len(word) > 2 and word not in easy_words:
            cleared_words.append(word)
    return cleared_words


# def write_word_to_file(input_data: str):
#     with open('get_all_words_from_text/easy_words.txt', 'a') as text_file:
#         text_file.write(f'{input_data}\n')


def add_word_to_file(input_data):
    print(f"{Fore.BLUE}{input_data}{Fore.RESET}\nwill be ignore in future")
    add_word_to_txt(input_data, easy_words_txt_file)
    # it is important to remove easy word from word_to_learn.txt ay first remove it from list "clear_words"


def make_choice(word):
    os.system('clear')
    pyperclip.copy(word)
    choice = input(
        f"\nIs word {Fore.GREEN}{word}{Fore.RESET} easy or you want ignore it?\n{Fore.RED}Press Y{Fore.RESET} or "
        f"{Fore.RED}Press N{Fore.RESET}\n")

    while choice.lower() != 'y' and choice.lower() != 'n':
        choice = input(f"{Fore.GREEN}Please print{Fore.RESET}\n{Fore.RED}Y - to continue{Fore.RESET}\n"
                       f"{Fore.RED}N - to stop{Fore.RESET}\n")
    if choice.lower() == 'y':
        add_word_to_file(word)  # fiunction that add easy word to txt file

    elif choice.lower() == 'n':
        os.system('clear')
        print(f'{Fore.GREEN} Lets go to next word{Fore.RESET}')


def add_easy_word_to_ignore(clear_words, word_len: int):
    for _ in clear_words:
        if len(_) == word_len:
            make_choice(_)


if __name__ == '__main__':
    easy_words_txt_file = 'get_all_words_from_text/easy_words.txt'
    words_to_learn_file = 'get_all_words_from_text/words_to_learn.txt'
    path_to_book_file = '/Volumes/big4photo/Downloads/Lamb to the Slaughter.txt'
    word_len = 6

    if Path(words_to_learn_file).exists():  # if book was lemmatized - cleared words were saved in words_to_learn.txt
        print('read words from file')
        clear_words = read_words_file(words_to_learn_file)  # words from words_to_learn.txt will be used

    else:  # no file words_to_learn.txt and book will be lemmatized first time
        words_from_text = lemma_word_from_text_file(path_to_book_file)
        print(f'words in text = {len(words_from_text)}')
        clear_words = clear_words_collection(words_from_text)
        for _ in clear_words:
            add_word_to_txt(_, words_to_learn_file)
        # i want to save cleared words for future optimisation  !!!!
        print(f'words after removing trash = {len(clear_words)}')

    add_easy_word_to_ignore(clear_words, word_len)
