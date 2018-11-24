import re
from pyphen import Pyphen 
import string
exclude = list(string.punctuation)

def sentence_splitter(text):
    sent_list = re.split(' *[\.\?!][\'"\)\]]* ', text)
    return sent_list
 
def text_len_sent(text):
    TL_sent = len(sentence_splitter(text))
    return TL_sent
    
def text_len_words(text):
    TL_words = len(text.split())
    return TL_words
 
def avg_sentence_length(text):
    ASL = float(text_len_words(text)/text_len_sent(text))
    return round(ASL, 2)
    
    
def avg_sent_per_word(text):
    ASPW = float(text_len_sent(text)/text_len_words(text))
    return round(ASPW, 2)
    
    
def char_count(text, ignore_spaces=True):
    if ignore_spaces:
        text_chars = text.replace(" ", "")
    return len(text_chars) 

    
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
    ASYPW = float(float(syllable_count(text))/float(len(text.split())))
    return round(ASYPW, 2)
    

def avg_syllab_per_sent(text):
    ASYPS = float(float(syllable_count(text))/float(len(sentence_splitter(text))))
    return round(ASYPS, 2)    
    
def diffsyll(text):
    count = 0
    for word in text.split():
        wrds = syllable_count(word)
        #if wrds >= 3:
        if wrds >= 4:
            count += 1
    return count

def percent_syll(text):
    perc_diff = float(float(diffsyll(text)))/float(len(text.split()))*100
    return round(perc_diff, 2) 
    
      
def get_simple_metrics(text):
    SL = len(sentence_splitter(text))
    WC = len(text.split())
    ASL = avg_sentence_length(text)
    TC = char_count(text)
    ALPW = avg_letter_per_word(text)
    ALPS = avg_letter_per_sent(text)
    SYC = syllable_count(text)
    ASYPW = avg_syllab_per_word(text)
    ASYPS = avg_syllab_per_sent(text)
    DW = diffsyll(text)
    ADF = percent_syll(text)
    return [SL, WC, ASL, TC, ALPW, ALPS, SYC, ASYPW, ASYPS, DW, ADF] 
    


    
def print_simple_metrics(text):
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
    print('Процент сложных слов в тексте', percent_syll(text))
    


       
       
    


