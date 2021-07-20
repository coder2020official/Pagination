from telebot import types

main = types.InlineKeyboardMarkup() # Button object
main.add(types.InlineKeyboardButton('⏮',callback_data="-1"),types.InlineKeyboardButton('⏭',callback_data="+1")) # Markups