from get_all_words_from_text.clear_list_of_words import remove_easy_words
from get_all_words_from_text.file_name_from_path import file_name_with_ext
from get_all_words_from_text.known_words import some_random_words
from get_all_words_from_text.use_txt_file import read_words_file, add_word_to_txt, create_file_if_no, \
    write_list_and_replace
from lemmatize_book import lemma_word_from_text_file
from pathlib import Path

if __name__ == '__main__':
    path_to_book_file = '/Volumes/big4photo/Downloads/Lamb to the Slaughter.txt'
    book_title = file_name_with_ext(path_to_book_file)  # get title of the book
    if Path(f'words_to_learn_file-{book_title}').exists():  # check existing of the file words_to_learn-book_title.txt
        # if no such file get lemma words from book if  words_to_learn-book_title.txt exist go to line
        print("use words from file")

    else:
        lemma_words = lemma_word_from_text_file(path_to_book_file)  # get lemma words from book
        for word in lemma_words:
            add_word_to_txt(word, f'words_to_learn_file-{book_title}')  # save this collection for future use
        #  and save words in file words_to_learn-book_title.txt
    # create list of all words from  words_to_learn-book_title.txt
    all_words = read_words_file(f'words_to_learn_file-{book_title}')  # all words in the  book
    all_words_count = len(all_words)
    print(f'{all_words_count = }')
    # check existing of the file easy_words.txt and create it if NO
    create_file_if_no('easy_words.txt')
    easy_word = read_words_file('easy_words.txt')
    easy_word_count = len(easy_word)
    print(f'{easy_word_count =}')
    # clear list of all words from words with two letters and words from easy_words_list
    cleared_words = remove_easy_words(all_words, easy_word)
    print(f"{len(cleared_words) = }")

    write_list_and_replace(cleared_words,
                           f'words_to_learn_file-{book_title}')  # overwrire words_to_learn file with clear words
    cleared_words.clear()  # clear list for future work

    all_words = read_words_file(f'words_to_learn_file-{book_title}')
    some_random_words(all_words, 10)
    print(f'{all_words_count = }')
    print(f'{all_words_count - len(all_words)} easy words added')



    # test words from list of all words ( may be by some len or by some number
    # and write easy words to txt file and save it to list
    # after all remove easy words from list of all words
    # overwrite file with list of all words
