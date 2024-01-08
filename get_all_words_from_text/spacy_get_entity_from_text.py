import spacy


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
