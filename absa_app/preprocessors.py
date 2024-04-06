import re
import spacy
import pickle
from torchtext.data import get_tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


nlp = spacy.load('en_core_web_sm')
torch_tokenizer = get_tokenizer('basic_english')

def lemmatize_text(text):
    # Process the text
    doc = nlp(text)
    
    # Extract the lemma for each token and join
    lemmatized_output = " ".join([token.lemma_ for token in doc if not token.is_stop])
    return lemmatized_output


def preprocess(text):
    """ Method to Clean Text """
    text = re.sub("[^a-zA-Z]", " ", text.replace('&', 'and').lower()) 
    text = lemmatize_text(text)
    return text


def load_pickled_file(filename):
    with open(filename, 'rb') as file:
        obj = pickle.load(file)

    return obj
