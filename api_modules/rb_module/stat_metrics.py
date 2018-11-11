import re
import os
import ksslib.readability_metrics as ksms
import string
exclude = list(string.punctuation)


def flesch_RE(text):
    ASL = ksms.avg_sentence_length(text)
    ASW = ksms.avg_syllab_per_word(text)
    FRE = 206.835 - float(1.3 * ASL) - float(60.6 * ASW)
    return round(FRE, 2)

def flesch_kincaid_grade(text):
    ASL = ksms.avg_sentence_length(text)
    ASW = ksms.avg_syllab_per_word(text)
    #английский язык!
    #FKRA = float(0.39 * ASL) + float(11.8 * ASW) - 15.59
    #русский
    #FKRA = float(0.49 * ASL) + float(7.3 * ASW) - 16.59
    #Оборнева
    FKRA = float(0.5 * ASL) + float(8.4 * ASW) - 15.59
    return round(FKRA, 2)
    
def smog_index(text): 
    if len(ksms.sentence_splitter(text)) >= 3:
        SMOG = (1.043 * (30*(ksms.diffsyll(text)/len(ksms.sentence_splitter(text))))**.5) + 3.1291
        return round(SMOG, 2)
    else:
        return 0
        
        
def coleman_liau_index(text):
    L = round(ksms.avg_letter_per_word(text)*100, 2)
    S = round(ksms.avg_sent_per_word(text)*100, 2)
    CLI = float((0.058 * L) - (0.296 * S) - 15.8)
    return round(CLI, 2)


def dale_chall_score(text): #т.к. делаем сложные слова как 4 слога, все ок 
    word_count = len(text.split())
    count = word_count - ksms.diffsyll(text)
    per = float(count)/float(word_count)*100
    difficult_words = 100-per
    if difficult_words > 5: #дальше идет адаптация: вместо 0,0496 0,062
        score = (0.1579 * difficult_words) + (0.062 * ksms.avg_sentence_length(text)) + 3.6365
    else:
        score = (0.1579 * difficult_words) + (0.062 * ksms.avg_sentence_length(text))
    return round(score, 2)
    
    
def gunning_fog(text):
    grade = 0.4*(ksms.avg_sentence_length(text) + ksms.percent_syll(text))
    return round(grade,2)
       
def count_statistics(text):
    print('Russian Flesh reading Ease =', flesch_RE(text))
    print('Russian Flesh-Kincaid Grade =', flesch_kincaid_grade(text))
    print('Russian SMOG =', smog_index(text))
    print('Russian CLI =', coleman_liau_index(text))
    print('Russian DCH =', dale_chall_score(text))
    print('Russian Gunning Fog =', gunning_fog(text))
    
def statist_vectors(text):
    FRE = flesch_RE(text)
    FKG = flesch_kincaid_grade(text)
    SMOG = smog_index(text)
    CLI = coleman_liau_index(text)
    DCH = dale_chall_score(text)
    GF = gunning_fog(text)
    return [FRE, FKG, SMPG, CLI, DCH, GF]   
    
    
    
    
def statist_sum(text):
    average = (flesch_kincaid_grade(text)+smog_index(text)+coleman_liau_index(text)+dale_chall_score(text)+gunning_fog(text))/5
    return round(average,2)

def simple_classifire(text):
    level = statist_sum(text)
    if level > 0 and level <13 :
        return 1
    if level >= 13 and level < 17:
        return 2
    return 3
    