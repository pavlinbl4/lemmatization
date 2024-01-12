from pathlib import Path
import pickle
import spacy
import os

from get_all_words_from_text.language_detection import detect_text_language


# python -m spacy download ru_core_news_lg
# python -m spacy download en_core_web_trf
# python -m spacy download en_core_web_sm
# python -m spacy download ru_core_news_sm


def nlp_doc(book_title: str, text: str):
    # create sub folder to additional files
    os.makedirs(f'{Path().home()}/Documents/ANKI/TEXTS/{book_title}/', exist_ok=True)

    # save doc container in pickle file
    path_to_pickle_file = f'{Path().home()}/Documents/ANKI/TEXTS/{book_title}/pickle-{book_title}.pickle'
    if os.path.isfile(path_to_pickle_file):
        with open(path_to_pickle_file, 'rb') as doc_data_file:
            doc = pickle.load(doc_data_file)
        print(f'\"{book_title}\" pickle file exist. \nDoc read from file')

    else:
        # create doc container
        # assert isinstance(language, object)
        language = detect_text_language(text)

        if language == 'en':
            nlp = spacy.load("en_core_web_trf")
            print("English text")
        else:
            nlp = spacy.load("ru_core_news_lg")
            print("Russian text")


        doc = nlp(text)

        with open(path_to_pickle_file, 'wb') as doc_data_file:
            pickle.dump(doc, doc_data_file)
        print(f'pickle file for \"{book_title}\" created')
    return doc


if __name__ == '__main__':
    nlp_doc('Русская книга', 'Крокодилы летят на север')
