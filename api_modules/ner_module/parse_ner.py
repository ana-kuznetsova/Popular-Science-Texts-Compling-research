from bootstrap_ner import parse_user_text
from launch_tomita import detect_ner_tomita

def extract_ner(user_text: str) -> str:
    detect_ner_tomita(user_text)
    return parse_user_text()
        