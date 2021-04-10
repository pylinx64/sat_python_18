import telebot

# создание бота 
bot = telebot.TeleBot('1779940761:AAGGXR8GXB-ivcZO5BUavreq6VDHedkdmRw') # токен

#-------------------start-----------------------------------------------
@bot.message_handler(commands=['start'])
def start_message(message):
    # отправка сообщений
    print(message.chat.first_name, message.text)
    bot.send_message( message.chat.id , "Привет, я гречка-бот!👽")
#-------------------start-----------------------------------------------

#--------------------text-----------------------------------------------
@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text == 'привет':
        bot.send_message( message.chat.id, "ну хай")
    else:
        bot.send_message( message.chat.id, "я тебя не понял")
#--------------------text-----------------------------------------------

print('###bot run...')
bot.polling()
