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
    
#сравниваем предобработанные тексты со списками слов


def common_compare(text): 
    text_len = len(text.split())
    common_words = 0
    for word in text.split():
        if word in commons:
            common_words += 1
    return round((common_words/text_len)*100, 2)      
    
def rude_compare(text): 
    text_len = len(text.split())
    rude_words = 0
    for word in text.split():
        if word in rudes:
            rude_words += 1
    return round((rude_words/text_len)*100, 2)  
    
def talks_compare(text): #сраниваем текст со списком общих слов
    text_len = len(text.split())
    talk_words = 0
    for word in text.split():
        if word in talks:
            talk_words += 1
    return round((talk_words/text_len)*100, 2)  

    
def measure_find(text):
    words = text.split(' ')
    prefixes = ['дека','гекто','кило','мега','гига','тера','пета','экса','зетта','иотта','деци','санти','милли','микро','нано','пико','фемто','атто','зепто','иокто']
    reg = '|'.join(['{}\w.*'.format(prefix) for prefix in prefixes])
    summo = len([word for word in words if re.findall(reg, word)])
    text_meas = round((float(summo)/float(len(text.split())))*100, 2)
    return text_meas

    

    
def any_comparor(text, vocabular): #если нужно будет добавить еще один словарь не изменяя модуль
    text_len = len(text.split())
    common_words = 0
    for word in text.split():
        if word in vocabular:
            common_words += 1
    return round((common_words/text_len)*100, 2) 
    
    

def compare_all(text):
    talks = talks_compare(text)*100
    commons = common_compare(text)*100
    rudes = rude_compare(text)*100
    measures = measure_find(text)*100
    return [talks, commons, rudes, measures]
    
def print_compare_all(text):
    talks = talks_compare(text)*100
    commons = common_compare(text)*100
    rudes = rude_compare(text)*100
    measures = measure_find(text)*100
    print('Разговорные слова:', talks)
    print('Общие слова:', commons)
    print('Грубые слова:', rudes)
    print('Приставки СИ:', measures)
	