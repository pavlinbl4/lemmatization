from get_all_words_from_text.clear_list_of_words import remove_easy_words
from get_all_words_from_text.file_name_from_path import file_name_with_ext
from get_all_words_from_text.known_words import some_random_words
from get_all_words_from_text.use_txt_file import read_words_file, add_word_to_txt, create_file_if_no, \
    write_list_and_replace
from lemmatize_book import lemma_word_from_text_file
from pathlib import Path


def create_words_to_learn_or_skip(book_title):
    if Path(f'words_to_learn_file-{book_title}').exists():  # check existing of the file words_to_learn-book_title.txt
        # if no such file get lemma words from book if  words_to_learn-book_title.txt exist go to line
        print("use words from file")
    else:
        lemma_words = lemma_word_from_text_file(path_to_book_file)  # get lemma words from book
        for word in lemma_words:
            add_word_to_txt(word, f'words_to_learn_file-{book_title}')  # save this collection for future use


def main():
    book_title = file_name_with_ext(path_to_book_file)  # get title of the book
    create_words_to_learn_or_skip(book_title)  # make lemmatization of text or skip it



    # check existing of the file easy_words.txt and create it if NO
    create_file_if_no('easy_words.txt')
    easy_word = read_words_file('easy_words.txt')  # all known words
    easy_word_count = len(easy_word)  # number of easy words
    print(f'{easy_word_count = }')







    all_words = read_words_file(f'words_to_learn_file-{book_title}')
    all_words_count = len(all_words)  # number words before optimization
    if all_words_count == 0:
        print("NO UNKNOWN WORDS IN TEXT")
    else:
        print(f'continue test with {all_words_count = }')
        some_random_words(all_words, 5)

        cleared_words = remove_easy_words(all_words, easy_word)  # !!!!! I think this function must run only once ????
        print(f"{len(cleared_words) = }")

        write_list_and_replace(cleared_words,
                               f'words_to_learn_file-{book_title}')  # overwriеe words_to_learn file with clear words
        cleared_words.clear()  # clear list for future work




if __name__ == '__main__':
    # path_to_book_file = "/Volumes/big4photo/Documents/ANKI/james blunt you're beautiful.txt"
    # path_to_book_file = '/Volumes/big4photo/Documents/ANKI/ God Was Never on Your Side Motörhead .txt'
    # path_to_book_file = '/Volumes/big4photo/Documents/ANKI/A Word in Spanish Song by Elton John.txt'
    # path_to_book_file = '/Volumes/big4photo/Documents/ANKI/Sting.txt'
    # path_to_book_file = '/Volumes/big4photo/Documents/ANKI/The Three Little Pigs.txt'
    # path_to_book_file = '/Volumes/big4photo/Downloads/Lamb to the Slaughter.txt'
    # path_to_book_file = '/Volumes/big4photo/Documents/ANKI/The Pig.txt'
    path_to_book_file = '/Volumes/big4photo/Documents/ANKI/Perfect Strangers.txt'
    main()
