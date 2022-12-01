# Instalar as libs
# pip install --user gTTS
# pip install --user playsound

# import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#Funcao responsavel por falar 
def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br')
    #Salva o arquivo de audio
    tts.save('hello.mp3')
    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('hello.mp3')

# frase = ouvir_microfone()
cria_audio("Não entendi o que você falou!")