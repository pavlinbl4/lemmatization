# https://spacy.io/usage
import spacy
import re


def read_easy_words_file():
    with open('get_all_words_from_text/easy_words.txt', 'r') as text_file:
        return text_file.read().splitlines()


def only_words_lowercase(line: str) -> str:
    return ' '.join(re.findall(r'[a-z]+', line.lower()))


def extract_word_from_text_file(path_to_file: str) -> set:
    nlp = spacy.load('en_core_web_sm')
    lemmatized_sentence_all = set()
    with open(path_to_file, 'r') as text:
        for line in text:
            words = only_words_lowercase(line)
            doc = nlp(words.strip())
            lemmatized_sentence = {token.lemma_ for token in doc}
            lemmatized_sentence_all.update(lemmatized_sentence)
    return lemmatized_sentence_all


def clear_words_collection(lemmatised_set: set) -> list:
    cleared_words = []
    easy_words = read_easy_words_file()
    for word in lemmatised_set:
        if len(word) > 2 and word not in easy_words:
            cleared_words.append(word)
    return cleared_words


if __name__ == '__main__':
    path_to_file = '/Volumes/big4photo/Downloads/Lamb to the Slaughter.txt'
    # print(read_easy_words_file())
    words_from_text = extract_word_from_text_file(path_to_file)
    print(f'words in text = {len(words_from_text)}')
    clear_words = clear_words_collection(words_from_text)
    print(f'words after removing trash = {len(clear_words)}')
    for _ in clear_words:
        if len(_) == 4:
            print(_)
