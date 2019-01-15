import subprocess

def launch_tomita(user_text: str) -> None:
    command = 'echo "'+user_text+'" | \
    ./tomita-parser/build/bin/tomita-parser ./tomita-parser/build/bin/config.proto'

    subprocess.call(command, shell=True) 
