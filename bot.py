import telebot
import time
import logging
from telebot import apihelper
from telebot import types

from src import keys
from src import config
from src.parser import Parser

parser = Parser()

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

apihelper.proxy = {'http':'http://10.10.1.10:3128'}

bot = telebot.AsyncTeleBot('1684182818:AAEHMVPZLw2EwwJ_GCEQNHj-FJt293KFNyE')

@bot.message_handler(commands=['start'])
def start_message(message):
   bot.send_message(message.chat.id, config.START_MSG)



@bot.message_handler(regexp=r"\/i\d+")
def handle_imdb_id(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Узнать больше", callback_data="show_more")
    watch_button = types.InlineKeyboardButton(text="Смотреть онлайн", callback_data="watch")
    keyboard.add(callback_button)
    keyboard.add(watch_button)

    parser.parse_id(message.json['text'][2:])
    response, photo = parser.output, parser.photo

    if photo is not None:
        bot.send_message(message.chat.id,
                         "[]({}) {}".format(photo, response),
                         parse_mode='markdown', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, response, reply_markup=keyboard)



@bot.message_handler(content_types=['text'])
def handle_text(message):
    response = parser.parse_text(message.json['text'])
    bot.send_message(message.chat.id, response)



@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == "show_more":
            callback_button = types.InlineKeyboardButton(text="Коротко", callback_data="show_less")
            watch_button = types.InlineKeyboardButton(text="Смотреть онлайн", callback_data="watch")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button)
            keyboard.add(watch_button)
            response, photo = parser.full_output, parser.photo
            if photo is not None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="[]({}) {}".format(photo, response), parse_mode='markdown',
                                      reply_markup=keyboard)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=response, reply_markup=keyboard)
        if call.data == "show_less":
            callback_button = types.InlineKeyboardButton(text="Узнать больше", callback_data="show_more")
            watch_button = types.InlineKeyboardButton(text="Смотреть онлайн", callback_data="watch")
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(callback_button)
            keyboard.add(watch_button)
            response, photo = parser.output, parser.photo
            if photo is not None:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="[]({}) {}".format(photo, response), parse_mode='markdown',
                                      reply_markup=keyboard)
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=response, reply_markup=keyboard)
        if call.data == "watch":
            back_button = types.InlineKeyboardButton(text="Назад", callback_data="show_less")
            ivi_button = types.InlineKeyboardButton(text="IVI", url=config.LINK_IVI + parser.name)
            okko_button = types.InlineKeyboardButton(text="OKKO", url=config.LINK_OKKO + parser.name)
            amedia_button = types.InlineKeyboardButton(text="AMEDIATEKA", url=config.LINK_AMEDIATEKA + parser.name)
            wink_button = types.InlineKeyboardButton(text="WINK", url=config.LINK_WINK + parser.name)
            megogo_button = types.InlineKeyboardButton(text="MEGOGO", url=config.LINK_MEGOGO + parser.name)
            start_button = types.InlineKeyboardButton(text="START", url=config.LINK_START + parser.name)
            premier_button = types.InlineKeyboardButton(text="PREMIER", url=config.LINK_PREMIER + parser.name)

            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(back_button)
            keyboard.add(ivi_button, okko_button, premier_button)
            keyboard.add(amedia_button, wink_button, megogo_button,start_button)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=config.WATCH_MSG, reply_markup=keyboard)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, )
        except Exception as e:
            logger.error(e)
            time.sleep(15)

