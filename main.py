from typing import Text
import telebot as tb
from telebot.types import Chat
from telebot import types

TOKEN = '5000887285:AAHjNN6dtwvIpCYzSglXGfFDXVQ4N_NmfB8'
botName ="MicroTigerBot"
bot = tb.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
   picture = open("picture/MikoIino.png", 'rb')
   bot.send_photo(message.chat.id, picture)
   bot.send_message(message.chat.id, "Hello,<b><i>{0.first_name}</i></b>.\n It`s <b><i>{1.first_name}</i></b>. Let`s work together!!".format(message.from_user, bot.get_me()), parse_mode='html')

markup = types.ReplyKeyboardMarkup(resize_keyboard= True)

celsius =types.KeyboardButton("Цельсий")
kelvin = types.KeyboardButton(" Кельвин")
fahrenheit = types.KeyboardButton("Фаренгейт")


markup.add(celsius, kelvin, fahrenheit)

@bot.message_handler(commands=['temperature'])
def temperature_message(message):
   bot.send_message(message.chat.id,"txt", reply_markup=markup)

@bot.message_handler(content_types='text')
def temperature_type_message(message):
   if(message.text == 'Цельсий' or message.text == 'Кельвин' or message.text == 'Фаренгейт'):
      bot.send_message(message.chat.id, "🌡 Определяю температуру в комнате... 🌡") 
      temperature = find_temperature()
      
      if(message.text == 'Цельсий'):
         temperature = str(temperature) + '°C'
      
      if(message.text == 'Кельвин'):
         temperature = str(temperature + 273) + 'K'
      
      if(message.text == 'Фаренгейт'):
         temperature = str(temperature * 1.8 + 32) + 'F'

      bot.send_message(message.chat.id, temperature , reply_markup=types.ReplyKeyboardRemove())
   else:
      bot.send_message(message.chat.id, "не совсем понял...")

def find_temperature():
   return 25.5 

bot.infinity_polling()