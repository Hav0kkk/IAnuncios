import subprocess

tts_path = ".\TTS.exe"
arguments = ["script.txt", "audio.mp3"]

try:
    subprocess.run([tts_path] + arguments, check=True)
    print("sucess!")
except subprocess.CalledProcessError:
    print("Erro")