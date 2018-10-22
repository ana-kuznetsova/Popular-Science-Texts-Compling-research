# Import modules
from typing import List
import bs4 as bs
from flashtext import KeywordProcessor
import re
import os
import pandas as pd
import pymorphy2
morph = pymorphy2.MorphAnalyzer()


# Define auxiliary functions

def _slurp(path):
    try:
        with open(path, 'r') as fo:
            text = fo.read()
    except UnicodeDecodeError:
        print(path)
        with open(path, 'r', encoding='cp1252') as fo:
            text = fo.read()
    return text


def _slurp_lines(path):
    with open(path, 'r') as fo:
        return [line.strip() for line in fo.readlines()]


def _compile_lemmas_list(input_path):
    lemmas_list = []
    for root, dirs, files in os.walk(input_path):
        for file_name in files:
            file_path = input_path + file_name
            lemmas = _slurp(file_path)
            lemmas = re.findall(r'[а-яё]+', lemmas)
            lemmas_list.extend(lemmas)
    lemmas_list = list(set(lemmas_list))
    return lemmas_list


def _initialize_processor(words: List[str]) -> KeywordProcessor:
    processor = KeywordProcessor()
    processor.add_keywords_from_list(words)
    return processor

# Define text processing functions


def _parse_xml(xml_output):
    '''Parses xml output from tomita.
    Returns a list of raw names. 
    Names require further processing. '''
    xml = bs.BeautifulSoup(xml_output, 'lxml')
    names = xml.find_all('name')
    pattern = re.compile(r'val="([А-ЯЁ]+)">')
    names_ext = []
    for name in names:
        name = name.get('val')
        names_ext.append(name)
    names_ext = [name.title() for name in names_ext]
    return names_ext


def _delete_erroneous_words(names: list, kword_processor):
    potential_names = []

    for name in names:
        true_name = []
        for n in name.split():
            lemma = morph.parse(n.lower())[0].normal_form
            if not kword_processor.extract_keywords(lemma) == [lemma]:
                true_name.append(n.title())
        final_name = ' '.join(true_name)
        if final_name != '':
            potential_names.append(final_name)
    return potential_names


def parse_user_text() -> str:
    '''Executes the whole pipeline from xml to complete
    names list '''
    xml_output = _slurp('./tomita-parser/build/bin/names.xml')
    return 


# Import required files and word lists.

# Process common words
common_words = _compile_lemmas_list('./ner_lists/slovnik/')
lemmas_processor = _initialize_processor(common_words)

# Process geo terms
geo_terms = _slurp_lines('./ner_lists/geo_terms.txt')
geo_processor = _initialize_processor(geo_terms)

# Process corpora names
corpora_names = _slurp_lines('./ner_lists/full_names_list.txt_')
