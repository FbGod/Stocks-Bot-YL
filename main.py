import telebot
from telebot import types

import invest_portfile
import stock_information
import visualisation

bot = telebot.TeleBot('5850999800:AAGBeKbfmi79ljRueP3tPY3aTPa4KmTyRp4')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("💼 Анализ портфеля 💻")
    btn2 = types.KeyboardButton("📈 Информация по акции 📉")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text=f"Привет, {message.from_user.username}! Я - бот который поможет тебе получить сводку по "
                          f"инвестиционному портфелю или подробную информацию по акции!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def user_reply(message):
    if message.text == "💼 Анализ портфеля 💻":
        mesg = bot.send_message(message.chat.id,
                                f'Введите тикеры акций в формате: ' + '\n' + '\n' + '<b>ТИКЕР1-количество1, ТИКЕР2-количество2</b>' + '\n' + '\n' +
                                f'Пример: <b>YNDX.ME-2, AAPL-4</b>' + '\n' + '\n' + 'Разделитель - запятая и пробел, '
                                                                                    'для '
                                                                              'российских акций добавьте .ME в конце',
                                parse_mode='html')
        bot.register_next_step_handler(mesg, portfile_info)

    elif message.text == '📈 Информация по акции 📉':
        mesg = bot.send_message(message.chat.id,
                                f'Введите тикер акции: ', parse_mode='html')
        bot.register_next_step_handler(mesg, stock_info)
    elif message.text == 'meme':

        photo = open('C:/Users/PC/PycharmProjects/stocks_bot/hmm.gif', 'rb')
        bot.send_animation(message.chat.id, photo)


def portfile_info(message):
    bot.send_message(message.chat.id, 'Вычисляем баланс. Подождите...')
    text = message.text
    list_stocks = []
    try:
        for element in text.split(', '):
            stock, quantity = element.split('-')
            list_stocks.append([stock, int(quantity)])
        result = invest_portfile.get_all_information(list_stocks)
        types_, companies, industries, currencies = result[0], result[1], result[2], result[1]
        vis = visualisation
        try:
            types_vis = vis.visualize_type(types_)
            companies_vis = vis.visualize_companies(companies)
            industries_vis = vis.visualize_industries(industries)
            currencies_vis = vis.visualize_currencies(currencies)
            bot.send_photo(message.chat.id, types_vis)
            bot.send_photo(message.chat.id, companies_vis)
            bot.send_photo(message.chat.id, industries_vis)
            bot.send_photo(message.chat.id, currencies_vis)
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id, 'Ошибка в вводе или при получении/парсинге данных')

    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Ошибка в вводе данных')


def stock_info(message):
    st_in = stock_information
    bot.send_message(message.chat.id, 'Получаем информацию, подождите...')
    try:
        res = st_in.get_stock(message.text)
        title = res[0]
        image = res[1]
        print(res)
        bot.send_photo(message.chat.id, image, caption=title)
    except Exception as e:
        print(e)


bot.polling(none_stop=True)
