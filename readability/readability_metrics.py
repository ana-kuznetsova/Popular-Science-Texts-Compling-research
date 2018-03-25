import re
from pyphen import Pyphen 
import string
exclude = list(string.punctuation)

def sentence_splitter(text):
    sent_list = re.split(' *[\.\?!][\'"\)\]]* ', text)
    return sent_list
 
 
def avg_sentence_length(text):
    tl = len(text.split())
    sn = len(sentence_splitter(text))
    ASL = float(tl/sn)
    return round(tl/sn, 1)
    
    
def avg_sent_per_word(text):
    sn = len(sentence_splitter(text))
    tl = len(text.split())
    ASPW = float(sn/tl)
    return round(ASPW, 2)
    
    
def char_count(text, ignore_spaces=True):
    if ignore_spaces:
        text = text.replace(" ", "")
    return len(text) 

    
def avg_letter_per_word(text):
    ALPW = float(float(char_count(text))/float(len(text.split())))
    return round(ALPW, 2)
    

def avg_letter_per_sent(text):
    ALPS = float(float(char_count(text))/float(len(sentence_splitter(text))))
    return round(ALPS, 2)
    

def syllable_count(text): 
    text = text.lower()
    text = "".join(x for x in text if x not in exclude)
    dic = Pyphen(lang='ru_RU')
    count = 0
    for word in text.split(' '):
        word_hyphenated = dic.inserted(word)
        count += max(1, word_hyphenated.count("-") + 1)
    return count
    
    
def avg_syllab_per_word(text):
    ALPW = float(float(syllable_count(text))/float(len(text.split())))
    return round(ALPW, 2)
    

def avg_syllab_per_sent(text):
    ALPW = float(float(syllable_count(text))/float(len(sentence_splitter(text))))
    return round(ALPW, 2)    
    
def diffsyll(text):
    count = 0
    for word in text.split():
        wrds = syllable_count(word)
        #if wrds >= 3:
        if wrds >= 4:
            count += 1
    return count
    
def simple_metrics(text):
    print('Количество предложений в тексте:', len(sentence_splitter(text)))
    print('Количество слов в тексте:', len(text.split()))
    print('Средняя длина предложений:', avg_sentence_length(text))
    print('Количество символов в тексте:', char_count(text))
    print('Средняя длина слова:', avg_letter_per_word(text))
    print('Средняя длина предложений в символах:', avg_letter_per_sent(text))
    print('Количество слогов в тексте:', syllable_count(text))
    print('Среднее количество слогов в слове:', avg_syllab_per_word(text))
    print('Среднее количеcтво слогов в предложении:', avg_syllab_per_sent(text))
    print('Количество сложных слов в тексте:', diffsyll(text))
    
def flesch_RE(text):
    ASL = avg_sentence_length(text)
    ASW = avg_syllab_per_word(text)
    FRE = 206.835 - float(1.3 * ASL) - float(60.6 * ASW)
    return round(FRE, 2)

def flesch_kincaid_grade(text):
    ASL = avg_sentence_length(text)
    ASW = avg_syllab_per_word(text)
    #английский язык!
    #FKRA = float(0.39 * ASL) + float(11.8 * ASW) - 15.59
    #русский
    #FKRA = float(0.49 * ASL) + float(7.3 * ASW) - 16.59
    #Оборнева
    FKRA = float(0.5 * ASL) + float(8.4 * ASW) - 15.59
    return round(FKRA, 1)
    
def smog_index(text): 
    if len(sentence_splitter(text)) >= 3:
        poly_syllab = diffsyll(text)
        SMOG = (1.043 * (30*(poly_syllab/len(sentence_splitter(text))))**.5) + 3.1291
        return round(SMOG, 1)
    else:
        return 0
        
        
def coleman_liau_index(text):
    L = round(avg_letter_per_word(text)*100, 2)
    S = round(avg_sent_per_word(text)*100, 2)
    CLI = float((0.058 * L) - (0.296 * S) - 15.8)
    return round(CLI, 2)


def dale_chall_score(text): #т.к. делаем сложные слова как 4 слога, все ок 
    word_count = len(text.split())
    count = word_count - diffsyll(text)
    per = float(count)/float(word_count)*100
    difficult_words = 100-per
    if difficult_words > 5: #дальше идет адаптация: вместо 0,0496 0,062
        score = (0.1579 * difficult_words) + (0.062 * avg_sentence_length(text)) + 3.6365
    else:
        score = (0.1579 * difficult_words) + (0.062 * avg_sentence_length(text))
    return round(score, 2)
    
    
def gunning_fog(text):
    per_diff_words = (diffsyll(text)/len(text.split())*100) + 5
    grade = 0.4*(avg_sentence_length(text) + per_diff_words)
    return round(grade,1)
       
def count_statistics(text):
    print('Russian Flesh reading Ease =', flesch_RE(text))
    print('Russian Flesh-Kincaid Grade =', flesch_kincaid_grade(text))
    print('Russian SMOG =', smog_index(text))
    print('Russian CLI =', coleman_liau_index(text))
    print('Russian DCH =', dale_chall_score(text))
    print('Russian Gunning Fog =', gunning_fog(text))
    
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
    

       
       
    


