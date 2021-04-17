# библиотека (устанавливается pip install pytelegrambotapi)
import telebot
from telebot import types


# создание бота 
bot = telebot.TeleBot('1779940761:AAGGXR8GXB-ivcZO5BUavreq6VDHedkdmRw') # токен

#-------------------start-----------------------------------------------
# ловит команду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # печатает в консоль кто писал
    print(message.chat.first_name, message.text)
    
    # создаем кнопку
    button = types.ReplyKeyboardMarkup()
    button.row('🧱', 'какой год?')
    button.row('по чем гречка?')
    
    # отправка сообщений
    bot.send_message( message.chat.id , "Привет, я гречка-бот!👽", reply_markup = button )
#-------------------start-----------------------------------------------

#--------------------text-----------------------------------------------
# ловит любой текcт от человека
@bot.message_handler(content_types=['text'])
def text_message(message):
    # проверяет текст: если привет то бот отвечает "ну хай"
    # на все остальное бот отвечает "я тебя не понял"
    if message.text == 'привет':
        bot.send_message( message.chat.id, "ну хай")
    elif message.text == 'по чем гречка?':
        bot.send_message( message.chat.id, '280 рублей' )
        bot.send_message( message.chat.id, 'https://rutxt.ru/files/13209/original/ede39c3cb2.JPG' )
    elif message.text == 'какой год?':
        
        bot.send_message( message.chat.id, '2077' )
    elif message.text == "🧱":
        bot.send_message(message.chat.id, 'ооо кирпичь! 🧱🧱🧱')
    else:
        bot.send_message( message.chat.id, "я тебя не понял")
#--------------------text-----------------------------------------------

# запускаем бота
print('###bot run...')
bot.polling()
