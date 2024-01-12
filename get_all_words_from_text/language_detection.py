import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector


def get_lang_detector(nlp, name):
    return LanguageDetector(seed=82)  # We use the seed 42


def detect_text_language(text):


    nlp_model = spacy.load("en_core_web_sm")
    Language.factory("language_detector", func=get_lang_detector)
    nlp_model.add_pipe('language_detector', last=True)

    # Document level language detection

    doc = nlp_model(text)
    language = doc._.language
    return language['language']


def read_text_file(path_to_text_file):
    with open(path_to_text_file, 'r') as text_file:
        text = text_file.read()
    return text


if __name__ == '__main__':
    text = read_text_file('/Volumes/big4photo/Downloads/2354045.txt')
    print(detect_text_language(text))
