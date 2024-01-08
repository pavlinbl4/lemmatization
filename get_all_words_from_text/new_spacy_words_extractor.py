from pathlib import Path

from icecream import ic

from get_all_words_from_text.clear_list_of_words import remove_easy_words
from get_all_words_from_text.file_name_from_path import file_name_no_ext
from get_all_words_from_text.main_make_words_from_text import create_words_to_learn_or_skip, select_file
from get_all_words_from_text.nlp_doc import nlp_doc
from get_all_words_from_text.use_txt_file import read_words_file, write_list_and_replace, \
    create_file_if_no


def find_book_for_lemma():
    # select text file from gui
    path_to_book_file = select_file()
    # path_to_book_file = '/Users/evgenii/Documents/ANKI/TEXTS/Dolan\'s Cadillac.txt'

    # get title of the book
    book_title = file_name_no_ext(path_to_book_file)
    print(f'{book_title = }\n')
    return path_to_book_file, book_title


def new_spacy_lemma():
    # select text file from gui
    path_to_book_file, book_title = find_book_for_lemma()
    ic(book_title)
    ic(path_to_book_file)

    # check existing of the file easy_words.txt and create it if NO
    easy_words_path_to_txt = f'{Path().home()}/Documents/ANKI/TEXTS/easy_words.txt'
    create_file_if_no(easy_words_path_to_txt)

    # read text file
    with open(path_to_book_file, 'r') as txt:
        text = txt.read()

    # create nlp doc file and save it to pickle file, if pickle file was created early - read data from pickle
    doc = nlp_doc(book_title, text)

    # create ent set
    ent_set = set([ent.text for ent in doc.ents])

    # load list of easy words from txt file
    easy_words = read_words_file(easy_words_path_to_txt)

    # create list of filtered words
    words = [f'{token.lemma_.lower()}' for token in doc
             if token.is_alpha
             and token.text not in ent_set
             and token.text not in easy_words
             and len(token.lemma_) not in easy_words
             and len(token.text) > 2
             and len(token.lemma_) > 2]

    # strange but easy words are still in list - remove them again
    words = remove_easy_words(words, easy_words)

    # remove doubles in words
    cleared_words_list = set(words)
    # ic(Counter(optimised_words))

    # save lemma words to file
    path_to_words_file = create_words_to_learn_or_skip(book_title, words)

    # write_list_and_replace(cleared_words_list, all_words)
    ic(path_to_words_file)
    write_list_and_replace(cleared_words_list, path_to_words_file)

    # words_more_10_times_in_text = [word for word, count in Counter(words).items() if count > 10]


if __name__ == '__main__':
    new_spacy_lemma()
    # get_sentence_from_text('/Users/evgenii/Documents/ANKI/TEXTS/Dolan\'s Cadillac.txt')
    # get_sentence_from_text('/Users/evgenii/Documents/ANKI/TEXTS/Full Dark, No Stars - FAIR EXTENSION.txt')
