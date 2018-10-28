### Модуль для измерения различных метрик ридабилити

Пример использования для анализа корпуса текстов:

````
import rb_module.stat_metrics as rbm

def FRE(texts):
    return [rbm.flesch_RE(text) for text in texts]

def FKG(texts):
    return [rbm.flesch_kincaid_grade(text) for text in texts]

def SMOG(texts):
    return [rbm.smog_index(text) for text in texts]

scipop_FRE = FRE(classes['text'])
scipop_FKG = FKG(classes['text'])
scipop_SMOG = SMOG(classes['text']) 

````

На выходе получаем список значений по трем метрикам для каждого текста. 
Для одного текста, соответственно, можно просто использовать rbm.flesch_kincaid_grade(text).

Txt-файлы — словари терминов, общеупотребительных слов, и т.д.

pos_tags — разметка текстов по частям речи и подсчет доли в тексте каждой из них
dictionary_compare — вычисление доли общеупотребительных, разговорных, ргуательных слов и научных терминов
metrics — Базовые подсчеты (количество слов в тексте, средняя длина предложения, и т.д.).
stat_metrics  — использует metric для рассчета классических метрик ридабилити (все адаптированы под русский язык)

Все функции возвращают число или набор чисел.

Для работы со словарями тексты небходимо лемматизировать (есть в модуле, но на всякий случай вот)

````
def lemma_texts_df(texts):
    texts_list = [' '.join(kd.morphy_words(text)) for text in texts] 
    cleaned = pd.DataFrame({'col':texts_list})
    return cleaned
````

В модуле также прописаны функции типа "посчитать все метрики сразу", но они пока работают некорректно.

