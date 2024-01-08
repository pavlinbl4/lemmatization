import spacy
from icecream import ic


def get_sentence_from_text(path_to_text_file: str):
    # get sentence from text
    ic(path_to_text_file)

    # read text file
    with open(path_to_text_file, 'r') as txt:
        text = txt.read()

    # create doc object
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    ic(len(text))
    ic(len(doc))

    for token in doc:
        if token.is_alpha:
            print(f'{token} --- {token.sent}')