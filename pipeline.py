import nltk
from preprocessing.cleaner import clean_text
from preprocessing.tokenizer import tokenize
from preprocessing.pos_tagger import pos_tag
from preprocessing.stop_words import remove_stopwords
from preprocessing.lemmatizer import lemmatize


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger_eng')


def preprocess_pipeline(text):
    cleaned = clean_text(text)
    tokens = tokenize(cleaned)
    no_stop = remove_stopwords(tokens)
    tagged = pos_tag(no_stop)
    lemmatized = lemmatize(tagged)
    return lemmatized