import speech_recognition as sr 
import pyttsx3
import pyaudio
import os
import sys
import datetime
import random
import time
import webbrowser
import setuptools.dist as distutils


# r = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Скажите что-нибудь ...")
#     audio = r.listen(source)

# quary = r.recognize_google(audio,Language="ru-RU")
# print("Вы казали:" + quary.lower())


import speech_recognition as sr


def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
talk("Добро пожаловать")


# Инициализация распознавателя
r = sr.Recognizer()
    
# Распознавание речи с использованием Google Web Speech API   
while True: 
 with sr.Microphone() as source:
        print('Скажите что-нибудь...')
        audio = r.listen(source)
        
# Это выполнение различных команд    
 try:
     text = r.recognize_google(audio, language="ru-RU").lower()
     print(f"Вы сказали: {text}")
     if 'привет' in text:
        print('Привет, я jarvis')
        talk('привет, я jarvis')
     elif 'ты молодец' in text:
        print('Рад стараться')
        talk('Рад страться')    
        sys.exit()
     elif 'скажи сколько время' in text:
         now  = datetime.datetime.today()
         time = now.strftime('%H:%M:%S')
         print(time)
         talk(time)
     elif 'открой браузер' in text:
         webbrowser.open('https://')
         talk('Открываю')
     elif 'открой youtube' in text:
         webbrowser.open('https://youtube.com/')
         talk('Открываю')
     elif 'включи музыку' in text:
         talk('Открываю')
         webbrowser.open('https://vk.com/id638350475')
     elif 'отдохни' in text:
         word = text.split()
         word.pop(0) and word.pop(1)
         words = ' '.join(word)
         time.sleep(int(words))
         talk('Я вернулся')
     elif 'аниме' in text:
         l = text.split()
         a= ' + '.join(l)
         webbrowser.open(f'https://yandex.ru/search/?text={a}')
         
         
         
 except IndexError:
     print('Ошибка...') 
         
 except sr.UnknownValueError:
    print('Не удалось распознать...')
    
    



    
        








# def talk(word):
#     engine = pyttsx3.init()
#     engine.say(word)
#     engine.runAndWait()
# talk("На данный момент время")  
# talk(time) 
  
while True:
    
 res = input().lower()
 
 if 'веббраузер' in res :
     webbrowser.open('https://') 

 elif 'аниме' in res :   
     word = res.split()
     result = ' + '.join(word)
     webbrowser.open(f'https://yandex.ru/search/?text={result}')
 elif 'браузер' in res:
     word = res.split()
     word.pop(0)
     words = ' + '.join(word)
     webbrowser.open(f'https://yandex.ru/search/?text={words}')
   


