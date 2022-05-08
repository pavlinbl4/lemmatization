# https://spacy.io/usage
import spacy
import re

nlp = spacy.load('en_core_web_sm')

lemmatized_sentence_all = set()
with open('/Volumes/big4photo/Documents/Documents_main/learn_English/Night Shift - The Boogeyman.txt', 'r') as text:
    for line in text:
        words = ' '.join(re.findall(r'[a-z]+',line.lower()))
        doc = nlp(words.strip())
        lemmatized_sentence = {token.lemma_ for token in doc}
        lemmatized_sentence_all.update(lemmatized_sentence)



# lemmatized_sentence = {token.lemma_ for token in doc}
with open('/Volumes/big4photo/Documents/Documents_main/learn_English/The Boogeyman_words.txt','a') as file:
    for word in lemmatized_sentence_all:
        if len(word) > 2:
            print(word)
            file.write(f'{word}\n')

print(len(lemmatized_sentence_all))