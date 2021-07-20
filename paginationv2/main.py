import config # config file with token
import telebot # bot library
from telebot import types
bot = telebot.TeleBot(config.TOKEN) # bot from TeleBot class

#handlers
@bot.message_handler(commands=['start'])
def welcomer(message):
    with open("photos/1.jpg","rb") as photo_file: # Open file-photo
        main = types.InlineKeyboardMarkup() # Button object
        main.add(types.InlineKeyboardButton('⏮',callback_data=f"-1|1|{config.prefix}"),types.InlineKeyboardButton('⏭',callback_data=f"+1|1|{config.prefix}")) # Markups
        bot.send_photo(message.chat.id,photo_file,caption="Choose:",reply_markup=main)
@bot.callback_query_handler(func=lambda call:True)
def call_handler_processer(call):
    main = types.InlineKeyboardMarkup() # Button object
    
    full_data = call.data.split("|")
    num = int(full_data[1]) + int(full_data[0])
    if num > config.max_photos:
        num = 1
    if num == 0:
        num = 5
    main.add(types.InlineKeyboardButton('⏮',callback_data=f"-1|{str(num)}|{config.prefix}"),types.InlineKeyboardButton('⏭',callback_data=f"+1|{str(num)}|{config.prefix}")) # Markups
    get_photo_location = "photos/" + str(num) + ".jpg"
    with open(get_photo_location,"rb") as updated_file:
        bot.edit_message_media(media=types.InputMedia(type='photo', media=updated_file),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=main)

bot.polling()