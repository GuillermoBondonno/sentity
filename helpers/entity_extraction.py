#import spacy

#try:
#    nlp = spacy.load("en_core_web_lg")
#except: # If not present, we download
#    spacy.cli.download("en_core_web_lg")
#    nlp = spacy.load("en_core_web_lg")

#import pickle

#with open('named_entity_recognition/ner_pickle', 'rb') as f:
#    nlp = pickle.load(f)
from nltk import word_tokenize, pos_tag

def nlp(sentence):
    words = word_tokenize(sentence)
    tags = pos_tag(words)
    entities = []
    previous_determiner = False
    for word, tag in tags:
        if tag in ["NNP", "NNS", "NNPS"]:
            entities.append(word)
        elif tag == "NN":
            if previous_determiner:
                entities.append(word)

        if tag == "DT":
            previous_determiner = True
        else:
            previous_determiner = False

    return entities

def get_entities(sentence):
    """
    get the named entities from a sentence
    sentence: string
    returns a list of tuples [(entity, label), ...]
    """
    doc = nlp(sentence)
    return doc
    return [X.text for X in doc.ents] #to use with spacy



if __name__ == "__main__":
    import sys
    sentence = sys.argv[1]
    print(get_entities(sentence))