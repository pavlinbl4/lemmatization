# lemmatize text and create collection with words

import spacy
import re


def only_words_lowercase(line: str) -> str:
    return ' '.join(re.findall(r'[a-z]+', line.lower()))


def lemma_word_from_text_file(path_to_file: str) -> set:
    nlp = spacy.load('en_core_web_sm')
    lemmatized_sentence_all = set()
    with open(path_to_file, 'r') as text:
        for line in text:
            words = only_words_lowercase(line)
            doc = nlp(words.strip())
            lemmatized_sentence = {token.lemma_ for token in doc}
            lemmatized_sentence_all.update(lemmatized_sentence)
    return lemmatized_sentence_all


if __name__ == '__main__':
    path_to_book_file = '/Volumes/big4photo/Downloads/Lamb to the Slaughter.txt'
    print(len(lemma_word_from_text_file(path_to_book_file)))
    for index, word in enumerate(lemma_word_from_text_file(path_to_book_file)):
        if index < 3:
            print(word)
