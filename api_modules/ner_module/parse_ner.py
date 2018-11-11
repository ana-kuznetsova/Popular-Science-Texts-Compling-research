from bootstrap_ner import parse_user_text
from launch_tomita import detect_ner_tomita
import re

print('Start')
def extract_ner(user_text: str) -> list:
    detect_ner_tomita(user_text)
    names = parse_user_text(user_text)
    return names

def markup_ner(user_text: str) -> None:
    def tag_names(user_text: str, names:list):
        search_pattern = '|'.join(names)
        replace_pattern = '<\&\g<0>!\&'
        return re.sub(search_pattern, replace_pattern, user_text)

    detect_ner_tomita(user_text)
    names = parse_user_text(user_text)
    return tag_names(user_text, names)