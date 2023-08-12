from telebot.types import ReplyKeyboardMarkup, KeyboardButton

d1 = KeyboardButton('/начать')
scrape_kb = ReplyKeyboardMarkup(resize_keyboard=True)
scrape_kb.add(d1)
