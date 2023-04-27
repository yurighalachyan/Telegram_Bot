import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_KEY = '6100825272:AAEJE1HzapJazfRP7MQHpOSfRTTorKlPjdA'
bot = telebot.TeleBot('6100825272:AAEJE1HzapJazfRP7MQHpOSfRTTorKlPjdA')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('I am an individual looking to join a startup', callback_data='option1')
    button2 = InlineKeyboardButton('I am an entrepreneur', callback_data='option2')
    button3 = InlineKeyboardButton('I can provide mentorship to entrepreneurs', callback_data='option3')
    button4 = InlineKeyboardButton('I am an investor', callback_data='option4')
    button5 = InlineKeyboardButton('Other', callback_data='option4')
    keyboard.add(button1, button2, button3, button4, button5)

    # Send the user a message with the keyboard
    bot.send_message(message.chat.id, 'Hello! Please introduce yourself:', reply_markup=keyboard)

# Handle button clicks
@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == 'option1':
        bot.send_message(call.message.chat.id, 'Here is the group chat for you: https://t.me/+tZCt2Q69ixNhY2Ji')
    elif call.data == 'option3':
        bot.send_message(call.message.chat.id, 'Here is the group chat for you: https://t.me/+g2o5K9MkQvNjZDQy')
    elif call.data == 'option4':
        bot.send_message(call.message.chat.id, 'Here is the group chat for you: https://t.me/+fXDhYjFbxDY2Nzgy')
    elif call.data == 'option2':
        keyboard2 = InlineKeyboardMarkup(row_width=1)
        button1 = InlineKeyboardButton("Find a mentor", callback_data='option3')
        button2 = InlineKeyboardButton("Find a co-founder", callback_data="option1")
        button3 = InlineKeyboardButton("Network with people", callback_data="option4")
        keyboard2.add(button1, button2, button3)
        bot.send_message(call.message.chat.id, 'What would you like to do?', reply_markup=keyboard2)

bot.polling()