# script to find known words in words file and remove them to easy words file

from loguru import logger

import random
import pyperclip
from colorama import Fore
from get_all_words_from_text.use_txt_file import read_words_file

logger.disable(__name__)


def write_words_from_set(file_path: str, keywords: set):
    with open(file_path, 'w') as text_file:
        for k_word in keywords:
            text_file.write(k_word + '\n')


def make_choice(cleared_words: list, easy_words: set, value_to_test):
    logger.info(len(easy_words))
    # index for random words
    random_digits = random.sample(range(1, len(cleared_words)), value_to_test)

    for index in random_digits:

        word = cleared_words[index]
        choice = input(
            f"\nIs word {Fore.GREEN}{word}{Fore.RESET} easy or you want ignore it?\n{Fore.RED}Press Y{Fore.RESET} or "
            f"{Fore.RED}Press N{Fore.RESET}\n")

        while choice.lower() != 'y' and choice.lower() != 'n':
            choice = input(f"{Fore.GREEN}Please print{Fore.RESET}\n{Fore.RED}Y - to continue{Fore.RESET}\n"
                           f"{Fore.RED}N - to stop{Fore.RESET}\n")

        # function that add easy word to set
        if choice.lower() == 'y':
            logger.debug(len(easy_words))
            easy_words.add(word)
            logger.debug(word)
            logger.debug(easy_words)
            logger.debug(len(easy_words))

        elif choice.lower() == 'n':
            pyperclip.copy(word)  # save to clip only unknown words
            # os.system('clear')
            print(f'{Fore.GREEN} Lets go to next word{Fore.RESET}')

    return easy_words


if __name__ == '__main__':
    # logger.add('logs/log.log')
    logger.disable('logs/log.log')

    all_words_path = '/Users/evgeniy/Documents/ANKI/TEXTS/words_from_all_file.txt'
    easy_words_path = '/Users/evgeniy/Library/Mobile Documents/com~apple~CloudDocs/ANKI/TEXTS/easy_words.txt'

    words_from_file: set = set(read_words_file(all_words_path))
    easy_words: set = set(read_words_file(easy_words_path))

    logger.info(len(words_from_file))
    logger.info(len(easy_words))
    logger.info(easy_words)

    words_from_file: set = words_from_file - easy_words
    logger.info(len(words_from_file))

    # updated easy_words set
    easy_words = make_choice(list(words_from_file), easy_words, value_to_test=3)
    logger.info(len(easy_words))

    # clear words from file again
    cleared_words_from_file: set = words_from_file - easy_words
    logger.info(len(cleared_words_from_file))
    logger.info(cleared_words_from_file)
    logger.info(easy_words)

    # write sets to text files
    write_words_from_set(all_words_path, words_from_file)
    write_words_from_set(easy_words_path, easy_words)
