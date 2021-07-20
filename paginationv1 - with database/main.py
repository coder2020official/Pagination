from connection import create_db_new, database_query


from photos import photos # photos

import config # config file with token

from markup import * # markup
import telebot # bot library

create_db_new()
bot = telebot.TeleBot(config.TOKEN) # bot from TeleBot class

#handlers
@bot.message_handler(commands=['start'])
def welcomer(message):
    with open("photos/1.jpg","rb") as photo_file: # Open file-photo
        bot.send_photo(message.chat.id,photo_file,caption="Choose:",reply_markup=main)
    is_in_db = database_query("SELECT * FROM users WHERE user_id = ?",(message.chat.id,)) # Check database for user
    if is_in_db == []:
        add_usr_db = database_query("INSERT INTO users VALUES(?,?,?)",(message.chat.id,message.from_user.id,1,))
    else:
        database_query("UPDATE users SET page = ? WHERE user_id = ?",(1,message.chat.id,))
@bot.callback_query_handler(func=lambda call:True)
def call_handler_processer(call):
    call_data_in_int = int(call.data)
    is_in_db = database_query("SELECT * FROM users WHERE user_id = ?",(call.message.chat.id,)) # Check database for user
    for i in is_in_db:
        new_value = int(i[2]) + call_data_in_int
        if len(photos) < new_value:
            new_value = 1
        if new_value == 0:
            new_value = len(photos)
        database_query("UPDATE users SET page = ? WHERE user_id = ?",(str(new_value),call.message.chat.id,))
        get_photo_location = photos.get(str(new_value))
        with open(get_photo_location,"rb") as updated_file:
            bot.edit_message_media(media=types.InputMedia(type='photo', media=updated_file),chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=main)

bot.polling()