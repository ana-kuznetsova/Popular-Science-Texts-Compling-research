import subprocess


def detect_ner_tomita(user_text: str) -> None:
    
    with open('/tomita-parser/build/bin/user_entry.txt', 'w') as fo:
        fo.write(user_text)

    subprocess.call("./tomita-parser/build/bin/tomita-parser config.proto", shell=True) 
