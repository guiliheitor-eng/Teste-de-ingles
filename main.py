import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random
import time
import asyncio



duration = 5  # segundos de gravação
sample_rate = 44100  


#Começo do jogo


while True:

    win_streak = 0

    words_by_level = {
        "fácil": ["🐱 gato", "🐶 cachorro", "🍎 maçã", "🥛 leite", "☀️ sol"],
        "médio": ["🏠 casa", "🏫 escola", "🤝 amigo", "🪟 janela", "💛 amarelo"],
        "difícil": ["💻 tecnologia", "🎓 universidade", "ℹ️ informação", "🗣️ pronúncia", "🧠 imaginação"]
    }



    dificuldade = input("Bem vindo ao Speak Right! Escolha o nível de dificuldade que voce quer do ingles (✨fácil, 🔥médio, 💀difícil): ").lower()

    palavra_escolhida = random.choice(words_by_level[dificuldade])


    print(f'A dificuldade foi escolhida:{dificuldade}, vamos prosseguir!!! Agora vc tera que falar a seguinte palavra:{palavra_escolhida}, porem em ingles')

    time.sleep(5)



    print("Fale agora...")
    recording = sd.rec(
    int(duration * sample_rate), # o número de amostras a serem registradas
    samplerate=sample_rate,      # taxa de amostras
    channels=1,                  # 1 significa gravação mono
    dtype="int16")               # tipo de dados para as amostras registradas
    sd.wait()  # aguardando o término da gravação


    wav.write("output.wav", sample_rate, recording)
    print("Gravação concluída, estou reconhecendo...")


    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)


    try:
        text = recognizer.recognize_google(audio, language="en")
        print("Você disse:", text)
        confirmaçao = input('Vc disse isso???(Sim ou Nao)').lower()
        if confirmaçao == 'sim':
            print('Ok!!! Sua resposta está')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')

            translator = Translator()
            translated = asyncio.run(
            translator.translate(text, src="en", dest="pt")
)
            if translated.text.lower().strip() == palavra_escolhida:
                print('Parabens, vc acertou👍👍👍')
                win_streak += 1
                print('Sua sequencia de acertos esta igual a:' + win_streak)
                
            

            else:
                print('😭 Vc errou!!')
                print('Essa era a resposta' + translated.text)
                

        else:
            print("Vamos tentar novamente, por favor reinicei o programa e tente novamente, lembre-se de falar a palavra em ingles")
        


    except sr.UnknownValueError:             # - se o Google não conseguiu entender a fala devido a ruídos ou silêncio
        print("A fala não pôde ser reconhecida.")
    except sr.RequestError as e:             # - se não houver conexão com a Internet ou a API estiver indisponível
        print(f"Service error: {e}")






