
# coding: utf-8

import pandas as pd
import os
from rutermextract import TermExtractor
import re
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("russian")

from pymystem3 import Mystem
m = Mystem()

from numpy import array


#частотный словарь
df = pd.read_csv('./filters/freqrnc2011.csv', sep='\t')
freq_dict = df[['Lemma','Freq(ipm)']]
sorted_freq = freq_dict.sort_values(by=['Freq(ipm)'])

lemmas = list(freq_dict['Lemma'])
values = list(freq_dict['Freq(ipm)'])

dictionary = dict(zip(lemmas, values))


#символьные n-граммы
with open('./filters/ngrams/bigrams.txt') as fl:
    bi = fl.read()
    
with open('./filters/ngrams/trigrams.txt') as fl:
    tri = fl.read()
    
with open('./filters/ngrams/tetragrams.txt') as fl:
    tetra = fl.read()
    
bigrams = bi.split('\n')
trigrams = tri.split('\n')
tetragrams = tetra.split('\n')


#части слова
with open('./filters/word_parts/suf2.txt') as fl:
    s2 = fl.read()

with open('./filters/word_parts/suf3.txt') as fl:
    s3 = fl.read()
    
with open('./filters/word_parts/suf4.txt') as fl:
    s4 = fl.read()

with open('./filters/word_parts/pref2.txt') as fl:
    p2 = fl.read()

with open('./filters/word_parts/pref3.txt') as fl:
    p3 = fl.read()

with open('./filters/word_parts/pref4.txt') as fl:
    p4 = fl.read()

suf2 = s2.split('\n')
suf3 = s3.split('\n')
suf4 = s4.split('\n')
pref2 = p2.split('\n')
pref3 = p3.split('\n')
pref4 = p4.split('\n')


#стоп-слова
with open('./filters/stopwords/stopwords.txt') as fl:
    SW = fl.read()
stopwords = SW.split('\n')


#извлекаем кандидатов, на вход подается текст как строка
def get_term_candidates(text):
    
    list_of_terms = []
    term_extractor = TermExtractor()

    for term in term_extractor(text):
        terms.append(term.normalized)
    return list_of_terms

def cand_preprocessing(list_of_candidates):
    term_unigrams = []
    term_bigrams = []
    term_trigrams = []
    term_multigrams = []

    lem_unigrams = []
    lem_bigrams = []
    lem_trigrams = []
    lem_multigrams = []

    for term in list_of_candidates:
        if len(term.split()) == 1:
            term_unigrams.append(term.lower())
            lem_unigrams.append(m.lemmatize(term))
        elif len(term.split()) == 2:
            term_bigrams.append(term.lower())
            lem_bigrams.append(m.lemmatize(term))
        elif len(term.split()) == 3:
            term_trigrams.append(term.lower())
            lem_trigrams.append(m.lemmatize(term))
        else:
            term_multigrams.append(term.lower())
            lem_multigrams.append(m.lemmatize(term))

    lem_uni = []

    for u in lem_unigrams:
        lem_uni.append(u[0])

    lem_bi = []
    for b in lem_bigrams:
        lem_bi.append([b[0],b[2]])

    lem_tri = []
    for t in lem_trigrams:
        lem_tri.append([t[0],t[2],t[4]])

    lem_multi = []

    for mul in lem_multigrams:
        mul = [x for x in mul if x != ' ']
        mul = mul[:-1]
        lem_multi.append(mul)
    return lem_uni, lem_bi, lem_tri, lem_multi


def freq_scores(list_of_terms):#проверяем частотность
    scores = []
    
    for term in list_of_terms:
        if term not in lemmas:
            scores.append(1)
        elif dictionary.get(term) < 20:
            scores.append(1)
        else:
            scores.append(0)
    return array(scores)



def pref_scores(list_of_terms):#проверяем начало слов
    scores1 = []
    
    for term in list_of_terms:
        if term[:-4] in pref4 == True:
            scores1.append(1)
        elif term[-3:] in pref3 == True:
            scores1.append(1)
        elif term[:-2] in pref2 == True:
            scores1.append(1)
        else:
            scores1.append(0)
    return array(scores1)


def suf_scores(list_of_terms):#проверяем конец слов
    scores2 = []
    
    for term in list_of_terms:
        t = stemmer.stem(term)
        if t[:4] in suf4 == True:
            scores2.append(1)
        elif t[:3] in suf3 == True:
            scores2.append(1)
        elif t[:2] in suf2 == True:
            scores2.append(1)
        else:
            scores2.append(0)
    return array(scores2)


def get_scores(list_of_terms):
    score1 = freq_scores(list_of_terms)
    score2 = suf_scores(list_of_terms)
    score3 = pref_scores(list_of_terms)
    
    total = score1 + score2 + score3
    cand_scores = dict(zip(list_of_terms, total))
    
    winners = []
    for candidate in cand_scores:
        if cand_scores.get(candidate) != 0:
            winners.append(candidate)
        else:
            continue
    
    return cand_scores, winners


def get_terms(text):
    
    candidates = get_term_candidates(text)
    lem_uni, lem_bi, lem_tri, lem_multi = cand_preprocessing(candidates)
    scores, winners = get_scores(lem_uni)
    terms = [term for term in winners if term not in stopwords]
    
    return terms

