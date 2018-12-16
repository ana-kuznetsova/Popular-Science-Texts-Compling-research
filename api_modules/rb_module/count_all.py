#import readability_old as readtrad
#from pos_tags import pos_stringer
#import pos_tags as pos_tags
#import readability_dictionary_compare as dict_metr

import re
import os
import string
from pyphen import Pyphen
import pymorphy2
import tqdm
import nltk
from string import punctuation
from collections import Counter


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
    ASL = float(text_len_words(text) / text_len_sent(text))
    return round(ASL, 2)


def avg_sent_per_word(text):
    ASPW = float(text_len_sent(text) / text_len_words(text))
    return round(ASPW, 2)


def char_count(text, ignore_spaces=True):
    if ignore_spaces:
        text_chars = text.replace(" ", "")
    return len(text_chars)


def avg_letter_per_word(text):
    ALPW = float(float(char_count(text)) / float(len(text.split())))
    return round(ALPW, 2)


def avg_letter_per_sent(text):
    ALPS = float(float(char_count(text)) / float(len(sentence_splitter(text))))
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
    ASYPW = float(float(syllable_count(text)) / float(len(text.split())))
    return round(ASYPW, 2)


def avg_syllab_per_sent(text):
    ASYPS = float(float(syllable_count(text)) / float(len(sentence_splitter(text))))
    return round(ASYPS, 2)


def diffsyll(text):
    count = 0
    for word in text.split():
        wrds = syllable_count(word)
        # if wrds >= 3:
        if wrds >= 4:
            count += 1
    return count


def percent_syll(text):
    perc_diff = float(float(diffsyll(text))) / float(len(text.split())) * 100
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


def stringer(text):
    stats = get_simple_metrics(text)
    sup = ('Количество предложений в тексте:', stats[0], 'Количество слов в тексте:', stats[1],
           'Средняя длина предложений:', stats[2],
           'Количество символов в тексте:', stats[3],
           'Средняя длина слова:', stats[4],
           'Средняя длина предложений в символах:', stats[5],
           'Количество слогов в тексте:', stats[6],
           'Среднее количество слогов в слове:', stats[7],
           'Среднее количеcтво слогов в предложении:', stats[8],
           'Количество сложных слов в тексте:', stats[9],
           'Процент сложных слов в тексте', stats[10])
    llist = list(sup)
    conc = ' '.join(str(x) for x in llist)
    return conc


def flesch_RE(text):
    ASL = avg_sentence_length(text)
    ASW = avg_syllab_per_word(text)
    FRE = 206.835 - float(1.3 * ASL) - float(60.6 * ASW)
    return round(FRE, 2)


def flesch_kincaid_grade(text):
    ASL = avg_sentence_length(text)
    ASW = avg_syllab_per_word(text)
    # английский язык!
    # FKRA = float(0.39 * ASL) + float(11.8 * ASW) - 15.59
    # русский
    # FKRA = float(0.49 * ASL) + float(7.3 * ASW) - 16.59
    # Оборнева
    FKRA = float(0.5 * ASL) + float(8.4 * ASW) - 15.59
    return round(FKRA, 2)


def smog_index(text):
    if len(sentence_splitter(text)) >= 3:
        SMOG = (1.043 * (30 * (diffsyll(text) / len(sentence_splitter(text)))) ** .5) + 3.1291
        return round(SMOG, 2)
    else:
        return 0


def coleman_liau_index(text):
    L = round(avg_letter_per_word(text) * 100, 2)
    S = round(avg_sent_per_word(text) * 100, 2)
    CLI = float((0.058 * L) - (0.296 * S) - 15.8)
    return round(CLI, 2)


def dale_chall_score(text):  # т.к. делаем сложные слова как 4 слога, все ок
    word_count = len(text.split())
    count = word_count - diffsyll(text)
    per = float(count) / float(word_count) * 100
    difficult_words = 100 - per
    if difficult_words > 5:  # дальше идет адаптация: вместо 0,0496 0,062
        score = (0.1579 * difficult_words) + (0.062 * avg_sentence_length(text)) + 3.6365
    else:
        score = (0.1579 * difficult_words) + (0.062 * avg_sentence_length(text))
    return round(score, 2)


def gunning_fog(text):
    grade = 0.4 * (avg_sentence_length(text) + percent_syll(text))
    return round(grade, 2)


def rb_vectors(text):
    FRE = flesch_RE(text)
    FKG = flesch_kincaid_grade(text)
    SMOG = smog_index(text)
    CLI = coleman_liau_index(text)
    DCH = dale_chall_score(text)
    GF = gunning_fog(text)
    return [FRE, FKG, SMOG, CLI, DCH, GF]


def rb_stringer(text):
    rb = rb_vectors(text)
    sup = ('Russian Flesh reading Ease =', rb[0],
           'Russian Flesh-Kincaid Grade =', rb[1],
           'Russian SMOG =', rb[2],
           'Russian CLI =', rb[3],
           'Russian DCH =', rb[4],
           'Russian Gunning Fog =', rb[5])
    llist = list(sup)
    rb_conc = ' '.join(str(x) for x in llist)
    return rb_conc


commons = open('common_lemmas.txt', 'r', encoding='utf-8')
commons = list(map(lambda x: x.strip(), commons))

rudes = open('rude.txt', 'r', encoding='utf-8')
rudes = list(map(lambda x: x.strip(), rudes))

talks = open('talks.txt', 'r', encoding='utf-8')
talks = list(map(lambda x: x.strip(), talks))

def common_compare(text):
    text_len = len(text.split())
    common_words = 0
    for word in text.split():
        if word in commons:
            common_words += 1
    return round((common_words / text_len) * 100, 2)


def rude_compare(text):
    text_len = len(text.split())
    rude_words = 0
    for word in text.split():
        if word in rudes:
            rude_words += 1
    return round((rude_words / text_len) * 100, 2)


def talks_compare(text):  # сраниваем текст со списком общих слов
    text_len = len(text.split())
    talk_words = 0
    for word in text.split():
        if word in talks:
            talk_words += 1
    return round((talk_words / text_len) * 100, 2)


def measure_find(text):
    words = text.split(' ')
    prefixes = ['дека', 'гекто', 'кило', 'мега', 'гига', 'тера', 'пета', 'экса', 'зетта', 'иотта', 'деци', 'санти',
                'милли', 'микро', 'нано', 'пико', 'фемто', 'атто', 'зепто', 'иокто']
    reg = '|'.join(['{}\w.*'.format(prefix) for prefix in prefixes])
    summo = len([word for word in words if re.findall(reg, word)])
    text_meas = round((float(summo) / float(len(text.split()))) * 100, 2)
    return text_meas


def compare_all(text):
    talks = talks_compare(text) * 100
    commons = common_compare(text) * 100
    rudes = rude_compare(text) * 100
    measures = measure_find(text) * 100
    return [talks, commons, rudes, measures]


def dict_stringer(text):
    dict = compare_all(text)
    sup = ('Разговорные слова:', dict[0],
           'Общие слова:', dict[1],
           'Грубые слова:', dict[2],
           'Приставки СИ:', dict[3])
    llist = list(sup)
    dict_conc = ' '.join(str(x) for x in llist)
    return dict_conc


morph = pymorphy2.MorphAnalyzer()


# предобработка

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


# подсчет частей речи

def count_all_pos(text):
    tagged = tag_pymorphy(text)
    words = tagged.split(' ')
    text_len = len(text.split())
    nouns = [word for word in words if re.findall('(NOUN)', word)]
    verbs = [word for word in words if re.findall('(INFN)', word)]
    preps = [word for word in words if re.findall('(PREP)', word)]
    conjs = [word for word in words if re.findall('(CONJ)', word)]
    adjs = [word for word in words if re.findall('(ADJF)', word)]
    all_nouns = round(((len(nouns)) / float(text_len)) * 100, 2)
    all_verbs = round(((len(verbs)) / float(text_len)) * 100, 2)
    all_preps = round(((len(preps)) / float(text_len)) * 100, 2)
    all_conjs = round(((len(conjs)) / float(text_len)) * 100, 2)
    all_adjfs = round(((len(adjs)) / float(text_len)) * 100, 2)
    return [all_nouns, all_verbs, all_preps, all_conjs, all_adjfs]


def pos_stringer(text):
    pos = count_all_pos(text)
    sup = ('NOUNS:', pos[0], 'VERBS:', pos[1],
           'PREPOSITIONS:', pos[2], 'CONJS:', pos[3],
           'ADJECTIVES:', pos[4])
    llist = list(sup)
    pos_conc = ' '.join(str(x) for x in llist)
    return pos_conc


def count_all_metrics(text):
    all_metr = [stringer(text), rb_stringer(text),
                pos_stringer(text), dict_stringer(text)]
    final = ' '.join(all_metr)
    return final
    
