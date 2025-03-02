import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# 替换为你的 Bot Token
TOKEN = 'YOUR_BOT_TOKEN'
# 替换为你的网页地址
WEBAPP_URL = 'YOUR_WEBAPP_URL'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('打开应用', web_app=WebAppInfo(url=WEBAPP_URL)))
    bot.send_message(message.chat.id, "点击下方按钮打开应用", reply_markup=markup)

if __name__ == "__main__":
    print("Bot 已启动...")
    bot.polling()