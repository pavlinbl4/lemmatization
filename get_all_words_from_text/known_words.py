import random
import os
import pyperclip
from colorama import Fore
from get_all_words_from_text.use_txt_file import add_word_to_txt


def make_choice(cleared_words,random_index):
    word = cleared_words[random_index]
    os.system('clear') # clear display in terminal
    # pyperclip.copy(word)  # save to clip only unknown words
    choice = input(
        f"\nIs word {Fore.GREEN}{word}{Fore.RESET} easy or you want ignore it?\n{Fore.RED}Press Y{Fore.RESET} or "
        f"{Fore.RED}Press N{Fore.RESET}\n")

    while choice.lower() != 'y' and choice.lower() != 'n':
        choice = input(f"{Fore.GREEN}Please print{Fore.RESET}\n{Fore.RED}Y - to continue{Fore.RESET}\n"
                       f"{Fore.RED}N - to stop{Fore.RESET}\n")
    if choice.lower() == 'y':
        add_word_to_txt(word, 'easy_words.txt')  # function that add easy word to txt file


    elif choice.lower() == 'n':
        pyperclip.copy(word)  # save to clip only unknown words
        os.system('clear')
        print(f'{Fore.GREEN} Lets go to next word{Fore.RESET}')



def some_random_words(cleared_words, value_to_test):  # test "value_to_test" words from list - are you know them?
    for _ in range(value_to_test):
        random_index = random.randint(0, len(cleared_words)-1)
        make_choice(cleared_words,random_index)


if __name__ == '__main__':
    some_random_words(['sdff', 'fox', 'dog', 'box', 'glass'], 3)
