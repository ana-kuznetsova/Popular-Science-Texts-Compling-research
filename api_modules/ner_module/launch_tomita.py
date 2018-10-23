import subprocess

user_text = 'профессор университета Альберт Эйнштейн предположил'

def detect_ner_tomita(user_text: str) -> None:
    
    with open('./tomita-parser/build/bin/user_entry.txt', 'w') as fo:
        fo.write(user_text)

    subprocess.call("./tomita-parser/build/bin/tomita-parser ./tomita-parser/build/bin/config.proto", shell=True) 
