import telebot
from telebot import types

bot = telebot.TeleBot('5850999800:AAGBeKbfmi79ljRueP3tPY3aTPa4KmTyRp4')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Анализ портфеля")
    btn2 = types.KeyboardButton("Информаця по акции")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text=f"Привет, {message.from_user.username}! Я - бот который поможет тебе получить сводку по "
                          f"инвестиционному портфелю или подробную информацию по акции!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def user_reply(message):
    if message.text == "Анализ портфеля":
        bot.send_message(message.chat.id,
                         f'Введите тикеры акций в формате: <b>ТИКЕР1-количество1, ТИКЕР2-количество2</b>'
                         f' пример: <b>YAN-2, AAPL-4</b>', parse_mode='html')
    elif message.text == 'Информаця по акции':
        bot.send_message(message.chat.id,
                         f'Введите тикеры акции: ', parse_mode='html')


bot.polling(none_stop=True)
