import re
import os
import pymorphy2
import tqdm
import nltk
from string import punctuation
from collections import Counter

morph = pymorphy2.MorphAnalyzer()

#предобработка

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
     

#подсчет частей речи
    
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
    
def pos_stringer(text):
    pos = count_all_pos(text)
    sup = ('NOUNS:', pos[0], 'VERBS:', pos[1],
    'PREPOSITIONS:', pos[2], 'CONJS:', pos[3],
    'ADJECTIVES:', pos[4])
    llist = list(sup)
    pos_conc = ' '.join(str(x) for x in llist)
    return pos_conc
