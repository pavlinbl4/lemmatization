import spacy
import re
import textract


from lemmatize_text_file.gui_files_tools import select_file_via_gui
from lemmatize_text_file.write_keywords import write_keywords_from_list


def textract_text_from_file(file_path):
    text = textract.process(file_path)
    return text.decode()


def lemmatize_text(text_file: str) -> set:
    nlp = spacy.load("ru_core_news_sm")
    text = textract_text_from_file(text_file)
    doc = nlp(text)
    lemmas = []
    for token in doc:
        lemmas.append(token.lemma_)
    return set(lemmas)


def set_to_string(input_set: set) -> str:
    output_string = ", ".join(str(elem) for elem in input_set)
    return output_string


def extract_only_cyrillic_words(many_words) -> list:
    # function takes a string, extracts words composed of letters and optional hyphens/asterisks
    # and returns a list of those extracted words
    if type(many_words) is list:
        text_string = ''.join(many_words)

    elif type(many_words) is set:
        text_string = set_to_string(many_words)

    elif type(many_words) is str:
        text_string = many_words

    pattern = r'[А-Яа-я]+\-*[А-Яа-я]+'  # only words in Cyrillic
    return re.findall(pattern, text_string)


def extract_only_cyrillic_words_to_set(string_with_some_words: str) -> set:
    pattern = r'[А-Яа-я]+\-*[А-Яа-я]+'  # only words in Cyrillic
    only_cyrilic_words = re.findall(pattern, string_with_some_words)
    return set(only_cyrilic_words)


def keywords_from_text_file(path_to_file: str) -> list:
    #  set from lemmatized text words
    all_words_from_text_set = lemmatize_text(path_to_file)

    # set from "bad_words"
    bad_words_set = extract_only_cyrillic_words_to_set('/Volumes/big4photo/Documents/keywords/bad_words.txt')

    # difference of two sets
    no_bad_words_set = all_words_from_text_set.difference(bad_words_set)

    # save only cyrillic words
    return extract_only_cyrillic_words(no_bad_words_set)


if __name__ == '__main__':
    path_to_file_with_text = select_file_via_gui()

    title = textract_text_from_file(path_to_file_with_text).split('\n')[:5]
    title = [i.strip() for i in title if len(i.strip()) > 3]
    title = "_".join(title[:2])

    keywords = keywords_from_text_file(path_to_file_with_text)

    write_keywords_from_list(keywords, f'/Users/evgeniy/Documents/keywords/{title}.txt')
    # save_data_to_txt_file(keywords, write_keywords_from_list)
