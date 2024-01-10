# script to find known words in words file and remove them to easy words file


import random
import pyperclip
from colorama import Fore
from icecream import ic

from get_all_words_from_text.clear_list_of_words import remove_easy_words
from get_all_words_from_text.remove_double_words_from_txt_file import main_remove_doubles_words_in_txt_file
from get_all_words_from_text.use_txt_file import add_word_to_txt, read_words_file, write_list_and_replace
from pathlib import Path


def make_choice(cleared_words, random_index):
    word = cleared_words[random_index]
    choice = input(
        f"\nIs word {Fore.GREEN}{word}{Fore.RESET} easy or you want ignore it?\n{Fore.RED}Press Y{Fore.RESET} or "
        f"{Fore.RED}Press N{Fore.RESET}\n")

    while choice.lower() != 'y' and choice.lower() != 'n':
        choice = input(f"{Fore.GREEN}Please print{Fore.RESET}\n{Fore.RED}Y - to continue{Fore.RESET}\n"
                       f"{Fore.RED}N - to stop{Fore.RESET}\n")

    # function that add easy word to txt file
    if choice.lower() == 'y':
        add_word_to_txt(word, f'{Path().home()}/Documents/ANKI/TEXTS/easy_words.txt')

    elif choice.lower() == 'n':
        pyperclip.copy(word)  # save to clip only unknown words
        # os.system('clear')
        print(f'{Fore.GREEN} Lets go to next word{Fore.RESET}')


def some_random_words(cleared_words, value_to_test):  # test "value_to_test" words from list - are you know them?
    used_indexes = []
    counter = 1
    while counter <= value_to_test:
        random_index = random.randint(0, len(cleared_words) - 1)
        if random_index not in used_indexes:
            used_indexes.append(random_index)
            counter += 1
            make_choice(cleared_words, random_index)


if __name__ == '__main__':
    all_words = '/Users/evgenii/Documents/ANKI/TEXTS/Full Dark, No Stars - FAIR EXTENSION/words_to_learn_file-Full Dark, No Stars - FAIR EXTENSION.txt'
    easy_words_path = f'{Path().home()}/Documents/ANKI/TEXTS/easy_words.txt'
    words_from_file = read_words_file(all_words)
    ic(len(words_from_file))
    some_random_words(words_from_file, 100)

    # new easy words added to test file, no good idea to optimise it
    main_remove_doubles_words_in_txt_file(easy_words_path)

    # now remove easy words from words file
    # remove easy words from file
    easy_words = read_words_file(easy_words_path)

    cleared_words_list = remove_easy_words(words_from_file, easy_words)
    ic(len(cleared_words_list))

    # write_list_and_replace(cleared_words_list, all_words)
    write_list_and_replace(cleared_words_list, all_words)
