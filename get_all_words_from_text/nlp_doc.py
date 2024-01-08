from pathlib import Path
import pickle
import spacy
import os


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
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)

        with open(path_to_pickle_file, 'wb') as doc_data_file:
            pickle.dump(doc, doc_data_file)
        print(f'pickle file for \"{book_title}\" created')
    return doc


if __name__ == '__main__':
    nlp_doc('Book Title', 'Simple text for test')
