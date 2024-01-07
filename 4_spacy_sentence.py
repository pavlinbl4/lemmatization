import spacy
from icecream import ic
from collections import Counter
from pathlib import Path
import pickle

from get_all_words_from_text.clear_list_of_words import remove_easy_words
from get_all_words_from_text.file_name_from_path import file_name_with_ext
from get_all_words_from_text.main_make_words_from_text import create_words_to_learn_or_skip, select_file
from get_all_words_from_text.remove_double_words_from_txt_file import main_remove_doubles_words_in_txt_file
from get_all_words_from_text.use_txt_file import read_words_file, add_word_to_txt, write_list_and_replace, \
    create_file_if_no


def get_sentence_from_text(path_to_text_file: str):
    # get sentence from text

    # read text file
    with open(path_to_text_file, 'r') as txt:
        text = txt.read()

    # create doc object
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    for number, sent in enumerate(doc.sents):
        # with open(f"/Users/evgenii/Documents/ANKI/TEXTS/FAIR EXTENSION - sentenses.txt", 'a') as output_file:
        #     output_file.write(sent.text + '\n\n')
        print(number, sent.text_with_ws)


def get_persons_from_text(path_to_text_file):

    # read text file
    with open(path_to_text_file, 'r') as txt:
        text = txt.read()

    # create doc object
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # find PERSON in doc
    persons_list = []
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            persons_list.append(ent.text)

            # print(ent.text, ent.label_)
    ic(len(persons_list))
    persons_set = set(persons_list)
    ic(len(persons_set))

    with open(f"/Users/evgenii/Documents/ANKI/TEXTS/FAIR EXTENSION - persons.txt", 'a') as output_file:
        for person in persons_set:
            output_file.write(person + '\n')


def new_spacy_lemma(path_to_book_file):
    # select text file from gui
    path_to_book_file = select_file()
    # path_to_book_file = '/Users/evgenii/Documents/ANKI/TEXTS/Full Dark, No Stars - FAIR EXTENSION.txt'

    # get title of the book
    book_title = file_name_with_ext(path_to_book_file)
    print(f'{book_title = }')

    # check existing of the file easy_words.txt and create it if NO
    create_file_if_no(f'{Path().home()}/Documents/ANKI/TEXTS/easy_words.txt')
    easy_words_path_to_txt = f'{Path().home()}/Documents/ANKI/TEXTS/easy_words.txt'

    # read text file
    with open(path_to_book_file, 'r') as txt:
        text = txt.read()

    # create doc object
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # create ent set
    ent_set = set([ent.text for ent in doc.ents])

    # load list of easy words from txt file
    easy_words = read_words_file(easy_words_path_to_txt)

    # save doc in pickle file
    path_to_pickle_file = f'{Path().home()}/Documents/ANKI/TEXTS/pickle-{book_title}.pickle'
    with open(path_to_pickle_file, 'wb') as doc_data_file:
        pickle.dump(doc, doc_data_file)


    # create list of words
    words = [f'{token.lemma_.lower()}' for token in doc
             if token.is_alpha
             and token.text not in ent_set
             and token.text not in easy_words
             and len(token.lemma_) not in easy_words
             and len(token.text) > 2
             and len(token.lemma_) > 2]

    # strange but easy words are still in list - remove them again
    words = remove_easy_words(words, easy_words)

    # add often words to easy words text file
    # for word, count in Counter(words).items():
    #     if count > 9:
    #         print(word)
    #         add_word_to_txt(word, easy_words_path_to_txt)


    # may be this bloke not useful
    k = 10
    founded_words = []
    while len([word for word, count in Counter(words).items() if count > k]) == 0 and k > 2:
        founded_words = ([word for word, count in Counter(words).items() if count > k])
        k -= 1

    # check founded words
    ic(founded_words)
    print(input('press any key'))

        # write it to easy words file
    for _ in founded_words:
        add_word_to_txt(_, easy_words_path_to_txt)

    # load list of easy words from txt file
    easy_words_path_to_txt = f'{Path().home()}/Documents/ANKI/TEXTS/easy_words.txt'
    easy_words = read_words_file(easy_words_path_to_txt)

    main_remove_doubles_words_in_txt_file(easy_words_path_to_txt)

    words = remove_easy_words(words, easy_words)

    # remove doubles in words
    cleared_words_list = set(words)
    # ic(Counter(optimised_words))

    # make lemmatization from text or skip it
    path_to_words_file = create_words_to_learn_or_skip(book_title, path_to_book_file)

    # write_list_and_replace(cleared_words_list, all_words)
    write_list_and_replace(cleared_words_list, path_to_words_file)









    # words_more_10_times_in_text = [word for word, count in Counter(words).items() if count > 10]





def find_all_ents(path_to_text_file):
    # read text file
    with open(path_to_text_file, 'r') as txt:
        text = txt.read()

    # create doc object
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    for ent in doc.ents:
        # if ent.label_ == 'CARDINAL':
        # if ent.label_ == 'GPE': - filter this
        # if ent.label_ == 'FAC': - filter this
        # if ent.label_ == 'EVENT': - filter this
        # if ent.label_ == 'DATE':   - filter this
        print(ent.text)
    ents = set([ent.label_ for ent in doc.ents])
    ic(ents)
    ic(type(ents))


if __name__ == '__main__':
    _path_to_text_file = '/Users/evgenii/Documents/ANKI/TEXTS/Full Dark, No Stars - FAIR EXTENSION.txt'
    # get sentence from text file
    # get_sentence_from_text(_path_to_text_file)

    # save persons from text to file
    # get_persons_from_text(_path_to_text_file)

    new_spacy_lemma(_path_to_text_file)

    # find_all_ents(_path_to_text_file)
