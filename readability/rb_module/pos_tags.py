import re
import os
import pymorphy2
import tqdm
import nltk
from string import punctuation
from collections import Counter


morph = pymorphy2.MorphAnalyzer()

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)
    
    
def tag_pymorphy(text):
    
    def find_tag(raw_tag):
        tag = re.findall('[A-Z]+', raw_tag)
        return tag[0]
    
    words = text.split()
    tags = [find_tag(str(morph.parse(w)[0].tag)) for w in words]
    tagged = []
    for word, tag in zip(words, tags):
        tagged.append(word)
        if (tag == 'UNKN' or tag == 'LATN'):
            tagged.append('')
        else:
            tagged.append('(' + tag + ')')
    return ' '.join(tagged)
    
    
def tag_me_all(texts):
    return [tag_pymorphy(text) for text in texts]    

    
def count_noun(text):
    tagged = tag_pymorphy(text)
    words = tagged.split(' ')
    text_len = len(text.split())
    nouns = [word for word in words if re.findall('(NOUN)', word)]
    return round(((len(nouns))/float(text_len))*100, 2)    
    
    
def all_nouns(texts):
    return [count_noun(text) for text in texts]
    
    
def count_verb(text):
    tagged = tag_pymorphy(text)
    words = tagged.split(' ')
    text_len = len(text.split())
    verbs = [word for word in words if re.findall('(INFN)', word)]
    return round(((len(verbs))/float(text_len))*100, 2)    
    
    
def all_verbs(texts):
    return [count_verb(text) for text in texts]
    
#а как сделать так, чтобы каждый раз морфик не запускать?    
    
def count_conj(text):
    tagged = tag_pymorphy(text)
    words = tagged.split(' ')
    text_len = len(text.split())
    conjs = [word for word in words if re.findall('(CONJ)', word)]
    return round(((len(conjs))/float(text_len))*100, 2)    
    
    
def all_conjs(texts):
    return [count_conj(text) for text in texts]
    
    
def count_prep(text):
    tagged = tag_pymorphy(text)
    words = tagged.split(' ')
    text_len = len(text.split())
    preps = [word for word in words if re.findall('(PREP)', word)]
    return round(((len(preps))/float(text_len))*100, 2)    
    
    
def all_preps(texts):
    return [count_prep(text) for text in texts]
    
    
def count_adj(text):
    tagged = tag_pymorphy(text)
    words = tagged.split(' ')
    text_len = len(text.split())
    adjs = [word for word in words if re.findall('(ADJF)', word)]
    return round(((len(adjs))/float(text_len))*100, 2)    
    
    
def all_adjs(texts):
    return [count_adj(text) for text in texts]
    
    
    
def count_any_word(text, term):
    tagged = tag_pymorphy(text)
    words = tagged.split(' ')
    text_len = len(text.split())
    counted = [word for word in words if re.findall(term, word)]
    return round(((len(counted))/float(text_len))*100, 2)    
         
def all_counted(texts, term):
    return [count_adj(text, term) for text in texts]
    
    
def count_all_pos(text):
    tagged = tag_pymorphy(text)
    words = tagged.split(' ')
    text_len = len(text.split())
    nouns = [word for word in words if re.findall('(NOUN)', word)]
    verbs = [word for word in words if re.findall('(INFN)', word)]
    preps = [word for word in words if re.findall('(PREP)', word)]
    conjs = [word for word in words if re.findall('(CONJ)', word)]
    adjs = [word for word in words if re.findall('(ADJF)', word)]
    all_nouns = round(((len(nouns))/float(text_len))*100, 2)
    all_verbs = round(((len(verbs))/float(text_len))*100, 2)
    all_preps = round(((len(preps))/float(text_len))*100, 2)
    all_conjs = round(((len(conjs))/float(text_len))*100, 2)
    all_adjfs = round(((len(adjs))/float(text_len))*100, 2) 
    return [all_nouns, all_verbs, all_preps, all_conjs, all_adjfs]
    
def count_all_all(texts):
    return [count_all_pos(text) for text in texts]
    


    