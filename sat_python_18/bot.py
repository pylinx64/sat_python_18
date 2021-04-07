import telebot

# создание бота 
bot = telebot.TeleBot('1779940761:AAGGXR8GXB-ivcZO5BUavreq6VDHedkdmRw')

#-------------------start-----------------------------------------------
@bot.message_handler(commands=['start'])
def start_message(message):
    # отправка сообщений
    print(message.chat.first_name, message.text)
    bot.send_message( message.chat.id , 'Привет, я гречка-бот!')
#-------------------start-----------------------------------------------



print('###bot run...')
bot.polling()

