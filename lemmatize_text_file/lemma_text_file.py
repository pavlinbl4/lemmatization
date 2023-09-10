import spacy

nlp = spacy.load('en_core_web_sm')


def lemmatize_text(text_file):
    with open(text_file) as f:
        text = f.read()

    doc = nlp(text)

    lemmas = []
    for token in doc:
        lemmas.append(token.lemma_)

    return set(lemmas)


if __name__ == '__main__':
    print(lemmatize_text('/Volumes/big4photo/Documents/ANKI/A Word in Spanish Song by Elton John.txt'))
