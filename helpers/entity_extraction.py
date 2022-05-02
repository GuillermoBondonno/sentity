import spacy
nlp = spacy.load("en_core_web_lg")
#import pickle

#with open('named_entity_recognition/ner_pickle', 'rb') as f:
#    nlp = pickle.load(f)



def get_entities(sentence):
    """
    get the named entities from a sentence
    sentence: string
    returns a list of tuples [(entity, label), ...]
    """
    doc = nlp(sentence)
    return [X.text for X in doc.ents]



if __name__ == "__main__":
    import sys
    sentence = sys.argv[1]
    print(get_entities(sentence))