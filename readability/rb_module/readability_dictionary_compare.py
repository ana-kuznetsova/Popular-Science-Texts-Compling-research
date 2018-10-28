import re
import os
import pandas as pd
import pymorphy2 as pm

commons = open('common_lemmas.txt', 'r', encoding = 'utf-8')
commons = list(map(lambda x:x.strip(), commons))

rudes = open('rude.txt', 'r', encoding = 'utf-8')
rudes = list(map(lambda x:x.strip(), rudes))

talks = open('talks.txt', 'r', encoding = 'utf-8')
talks = list(map(lambda x:x.strip(), talks))

#terms = open('terms.txt', 'r', encoding = 'utf-8')
#terms = list(map(lambda x:x.strip(), terms))
#предобработка текстов

morph = pm.MorphAnalyzer()

def morphy_words(text):
    nolinks = ' '.join([word for word in text.split() if (not re.findall('https?://|\w\.\w', word))])#удалили ссылки
    clean_line = re.sub('[\W\d_-]+', ' ', nolinks.lower().strip())
    ws = re.split(' +', clean_line)
    return [morph.parse(w)[0].normal_form for w in ws]
    
def lemma_texts_df(texts):
    texts_list = [' '.join(morphy_words(text)) for text in texts] 
    cleaned = pd.DataFrame({'col':texts_list})
    return cleaned
    
#сравниваем предобработанные тексты со списками слов


def common_compare(text): 
    text_len = len(text.split())
    common_words = 0
    for word in text.split():
        if word in commons:
            common_words += 1
    return round((common_words/text_len)*100, 2)      

def total_common(texts):
    return [common_compare(text) for text in texts]
    
    
def rude_compare(text): 
    text_len = len(text.split())
    rude_words = 0
    for word in text.split():
        if word in rudes:
            rude_words += 1
    return round((rude_words/text_len)*100, 2)  
    
def total_rude(texts):
    return [rude_compare(text) for text in texts]   
    
def talks_compare(text): #сраниваем текст со списком общих слов
    text_len = len(text.split())
    talk_words = 0
    for word in text.split():
        if word in talks:
            talk_words += 1
    return round((talk_words/text_len)*100, 2)  

    
def total_talks(texts):
    return [talks_compare(text) for text in texts]    
    
    
def measure_find(text):
    words = text.split(' ')
    prefixes = ['дека','гекто','кило','мега','гига','тера','пета','экса','зетта','иотта','деци','санти','милли','микро','нано','пико','фемто','атто','зепто','иокто']
    reg = '|'.join(['{}\w.*'.format(prefix) for prefix in prefixes])
    summo = len([word for word in words if re.findall(reg, word)])
    text_meas = round((float(summo)/float(len(text.split())))*100, 2)
    return text_meas

def measure_all(texts):
    return [measure_find(text) for text in texts]
    
    
#def terms_compare(text): #сраниваем текст со списком общих слов
#   text_len = len(text.split())
#    talk_words = 0
 #   for word in text.split():
 #       if word in terms:
#            terms_words += 1
#    return round((terms_words/text_len)*100, 2)  

#def terms_all(texts):
#    return [terms_find(text) for text in texts]
        
    
    
def any_comparor(text, vocabular): #если нужно будет добавить еще один словарь не изменяя модуль
    text_len = len(text.split())
    common_words = 0
    for word in text.split():
        if word in vocabular:
            common_words += 1
    return round((common_words/text_len)*100, 2) 
    
    
    
def total_any_comparor(texts, vocabular):
    return [any_comparor(text, vocabular) for text in texts]
    
    

def compare_all(text):
    talks = talks_compare(text)*100
    commons = common_compare(text)*100
    rudes = rude_compare(text)*100
    measures = measure_find(text)*100
    return [talks, commons, rudes, measures]
    