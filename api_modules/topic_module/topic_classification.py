# Imports
import sys
sys.path.append('C:\Program Files\Anaconda3\Lib\site-packages')

import pickle

import re
import pymorphy2
from stop_words import get_stop_words

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

def load_model(filename):
	with open(filename, 'rb') as file:
		model = pickle.load(file)
	return model

vect_model = load_model('./vectorize/model.pkl')
reduce_model = load_model('./reduce_dim/model.pkl')
classify_model = load_model('./classify/model.pkl')

def preprocess(text):
	morph = pymorphy2.MorphAnalyzer()
	stopwords = stopwords = get_stop_words('russian')
	words = re.findall(r'[a-zа-яё]+', text.lower())
	lemmas = [morph.parse(word)[0].normal_form for word in words if word not in stopwords]
	return [' '.join(lemmas)]
	
def vectorize(text, model):
	return model.transform(text)
	
# def reduce_dim(text_vec_matrix, model):
#	return model.transform(text_vec_matrix)

def classify(text_vec, model):
	return model.predict(text_vec.reshape(1, -1))
	
def get_topic(text, vectorizer = vect_model, reducer = reduce_model, classifier = classify_model):
	lemm_text = preprocess(text)
	vect_text = vectorize(lemm_text, vectorizer)
	if reducer:
		vect_text = vectorize(vect_text, reducer)
	return classifier.predict(vect_text[0].reshape(1, -1))[0]
	






