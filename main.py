import telebot as tb
from telebot.types import Chat


TOKEN = '5000887285:AAHjNN6dtwvIpCYzSglXGfFDXVQ4N_NmfB8'
botName ="MicroTigerBot"
bot = tb.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
   picture = open("picture/MikoIino.png", 'rb')
   bot.send_photo(message.chat.id, picture)
   bot.send_message(message.chat.id, "Hello,<b><i>{0.first_name}</i></b>.\n It`s <b><i>{1.first_name}</i></b>. Let`s work together!!".format(message.from_user, bot.get_me()), parse_mode='html')

bot.infinity_polling()