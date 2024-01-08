import spacy


def get_persons_from_text(path_to_text_file):
    # read text file
    with open(path_to_text_file, 'r') as txt:
        text = txt.read()

    # create doc object
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # find PERSON in doc
    persons_list = []
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            persons_list.append(ent.text)

            # print(ent.text, ent.label_)
    ic(len(persons_list))
    persons_set = set(persons_list)
    ic(len(persons_set))

    with open(f"/Users/evgenii/Documents/ANKI/TEXTS/FAIR EXTENSION - persons.txt", 'a') as output_file:
        for person in persons_set:
            output_file.write(person + '\n')