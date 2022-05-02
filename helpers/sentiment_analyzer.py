#import pickle
from helpers.entity_extraction import get_entities


#load the model
from transformers import pipeline
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")
                      
#with open('classifiers/facebook-bart-large-mnli', 'rb') as f:
#    classifier = pickle.load(f)

def classify(sentence, entity):
    """
    classify the sentiment of a sentence for a given entity
    params:
        sentence: string
        entity: string
    returns:
        dictionaty with the schema: {
            "labels" : positive, neutral or negative
            "scores" : list of floats adding up to 1
        }
    """
    labels = [f"positive about {entity}", f"negative about {entity}", f"neutral about {entity}"]
    pred = classifier(sentence, labels)
    
    #we dont want the sentence to appear in the return again, and we dont want the entity to appear in the labels
    del pred["sequence"]
    pred['labels'] = [l.replace(f" about {entity}", "") for l in pred['labels']]
    
    return pred

def extract_entities_and_analyze_sentiment(sentence):
    entities = get_entities(sentence)
    result = {}
    for entity in entities:
        sentiment = classify(sentence, entity[0])
        result[entity[0]] = sentiment

    return result

def analyze_for_given_entities(sentence, entities):
    result = {}
    for entity in entities:
        sentiment = classify(sentence, entity)
        result[entity] = sentiment

    return result

if __name__ == "__main__":
    import sys
    sentence = sys.argv[1]
    for e,s in extract_entities_and_analyze_sentiment(sentence).items():
        print(f"{e}: {s}")