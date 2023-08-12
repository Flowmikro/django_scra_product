from telebot.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/начать')
scrape_kb = ReplyKeyboardMarkup(resize_keyboard=True)
scrape_kb.add(b1)
