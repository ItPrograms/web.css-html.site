import webbrowser
from gc import callbacks
from io import open_code
from os import access, close
from time import sleep
import random

import telebot
# import pyttsx3
from telebot import types


bot = telebot.TeleBot('7523716138:AAG4yNy6iVNwPQMFlbP7YVl_mHi8f3oQrek')

# def talk(word):
#     engine = pyttsx3.init()
#     engine.say(word)
#     engine.runAndWait()
# talk("Добро пожаловать")

list = 'урок, python, hello'
word = list.split()
words = word.pop(0)
print(word)



@bot.message_handler(commands=['id'])
def start1(message):
    bot.send_message(message.chat.id,message)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'<b>🈯 Введите пароль 🈯</b>\n',parse_mode='html')
    # def talk(word):
    #     engine = pyttsx3.init()
    #     engine.say(word)
    #     engine.runAndWait()
    # talk("Введите пароль")





@bot.message_handler(content_types=['text'])
def text(message):
    text = message.text.strip().lower()
    if '567u89009' == text:
      # def talk(words):
      #    engine = pyttsx3.init()
      #    engine.say(words)
      #    engine.runAndWait()
      # talk("Вы успешно авторизировались")
      markup = types.InlineKeyboardMarkup()
      btn = types.InlineKeyboardButton('Как тебя зовут ?',callback_data='name')
      btn1 = types.InlineKeyboardButton('Меню',callback_data='mena')
      markup.add(btn,btn1)
      bot.send_message(message.chat.id,'Вы успешно авторизировались 💚',reply_markup=markup)


      @bot.callback_query_handler(func=lambda callback:True)
      def name(callback):
        if callback.data == 'name':
            bot.send_message(message.chat.id,'<b>Мой создатель дал мне имя "Jarvis"</b>',parse_mode='html')
            # talk("Мой создатель дал мне имя 'Jarvis'")
        elif callback.data == 'mena':
             # Если что посмотреть как делать с edit
             # talk("Мы предоставили ваши кнопки")
             bot.delete_message(callback.message.chat.id,callback.message.message_id)
             markup = types.InlineKeyboardMarkup()
             btn = types.InlineKeyboardButton('Python 🧑‍💻',callback_data='information')
             btn1 = types.InlineKeyboardButton('Назад 👈',callback_data='back')
             btn6 = types.InlineKeyboardButton('Песни 🎧',callback_data='songs')
             markup.add(btn,btn1,btn6)
             btn2 = types.InlineKeyboardButton('Записи ✍',callback_data='list')
             btn6 = types.InlineKeyboardButton('Поиск YT 🖥',callback_data='min')
             markup.add(btn2,btn6)
             btn1 = types.InlineKeyboardButton('Впн 🔥',callback_data='vpn')
             markup.add(btn1)
             btn1 = types.InlineKeyboardButton('Html 🌏',callback_data='html')
             markup.add(btn1)
             bot.send_message(message.chat.id,'Мы предоставили ваши кнопки 💚',reply_markup=markup)



        elif callback.data == 'vpn':
            webbrowser.open('PlanetVpn')


        elif callback.data == 'random':
            random1 = random.randint(1,90)
            bot.send_message(message.chat.id,random1)

        elif callback.data == 'min':
            bot.send_message(message.chat.id,'Например: "Поиск:" и ваш текст')


        elif callback.data == 'list':
            bot.answer_callback_query(callback_query_id=callback.id,show_alert=True,text='Напишите текст')

        elif callback.data == 'back':
            bot.delete_message(callback.message.chat.id,callback.message.message_id)
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton('Как тебя зовут ?',callback_data='name')
            btn1 = types.InlineKeyboardButton('Меню',callback_data='mena')
            markup.add(btn,btn1)
            bot.send_message(message.chat.id,'Вы успешно авторизировались 💚',reply_markup=markup)

        elif callback.data == 'songs':
            webbrowser.open('https://vk.com/audio638350475_456239062')

        elif callback.data == 'html':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Основы 10мин 🐣',url='https://www.youtube.com/watch?v=SKRydSA2bYA')
            btn2 = types.InlineKeyboardButton('Html 🧑‍💻',url='https://www.youtube.com/watch?v=oVqyRw3l3iI')
            btn3 = types.InlineKeyboardButton('Удалить ❌',callback_data='remove')
            markup.add(btn1,btn2,btn3)
            bot.send_message(message.chat.id,'Вся важная информация Html 💚',reply_markup=markup)

        elif callback.data == 'information':
             markup = types.InlineKeyboardMarkup()
             btn = types.InlineKeyboardButton('Видео OpenCv✈',url='https://www.youtube.com/watch?v=S-kg8eVPXRQ')
             btn1 = types.InlineKeyboardButton('Видео Управление Пк💻',url='https://www.youtube.com/results?search_query=простой+урок+pyautogui')
             markup.add(btn,btn1)
             btn2 = types.InlineKeyboardButton('Видео Python🥳',url='https://www.youtube.com/playlist?list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa')
             btn3 = types.InlineKeyboardButton('Удалить ❌',callback_data='remove')
             markup.add(btn2,btn3)
             bot.send_message(message.chat.id,'👉Все важная информация и кнопки 👈',reply_markup=markup)
        elif callback.data == 'affect':
            bot.answer_callback_query(callback_query_id=callback.id, show_alert=True, text='❤️ Error ❤️')
        elif callback.data == 'remove':
            bot.delete_message(callback.message.chat.id,callback.message.message_id)

    elif 'Текст' in message.text:
        bot.delete_message(message.chat.id,message.message_id)
        res = message.text.strip()
        word = res.split()
        word.pop(0)
        result = ' '.join(word)
        bot.send_message(message.chat.id,result)
    elif 'Поиск' in message.text:
        bot.delete_message(message.chat.id,message.message_id)
        res = message.text.strip()
        word = res.split()
        word.pop(0)
        result = '+'.join(word)
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('Открыть',url=f'https://www.youtube.com/results?search_query={result}')
        btn1 = types.InlineKeyboardButton('Удалить ❌',callback_data='remove')
        markup.add(btn,btn1)
        bot.send_message(message.chat.id,'Ваша ссылка ☺', reply_markup=markup)




    # else:
    #       markup = types.InlineKeyboardMarkup()
    #       btn = types.InlineKeyboardButton('👉Нажми👈',callback_data='affect')
    #       markup.add(btn)
    #       bot.delete_message(message.chat.id,message.message_id) and bot.send_message(message.chat.id,'💬 Я не понимаю таких сообщений 💬',reply_markup=markup)
    #       bot.send_message(message.chat.id,'🥶')
    #       def talk(words):
    #          engine = pyttsx3.init()
    #          engine.say(words)
    #          engine.runAndWait()
    #       talk("Я не понимаю таких сообщений")





 # bot.answer_callback_query(callback_query_id=callback.id, show_alert=False,text='Hello')


bot.polling(none_stop=True)
