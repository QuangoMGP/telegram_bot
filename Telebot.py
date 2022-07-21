import telebot
from telebot import types
from Keyboards import keyboard1, keyboard2
from Answers import answers, ComList
from usersbd import StealIDbd
FToken = open('token.txt', 'r')
token = FToken.read() #TODO упростить открытие файла
FToken.close()
bot = telebot.TeleBot(token)
def stealID(message):
    try:
        f = open('base.txt', 'r')
    except:
        f = open("base.txt", "w+")
        f.close()
        f = open('base.txt', 'r')
    Exist = 1 if str(message.chat.id) in f.read() else 0
    f.close()
    if Exist == 0:
        f = open('base.txt', 'a+')
        f.write(str(message.chat.id) + " ")
        try:
            f.write(str(message.chat.first_name) + " ")
        except:
            f.write("Error ")
        try:
            f.write(str(message.chat.last_name) + " ")
        except:
            f.write("Error ")
        f.write(str(message.chat.username) + " " + str(message.chat.location) + "\n")
        f.close()

@bot.message_handler(commands=['start'])
def start(message):
    try:
        stealID(message)
        #StealIDbd(message)
    except:
        print("Ошибка записи в бд у ID: " + str(message.chat.id))
        bot.send_message(404969882, message.chat.id)

    HelpInlineButton = types.InlineKeyboardButton("Help", callback_data='help')
    HelpInline = types.InlineKeyboardMarkup().row(HelpInlineButton)
    bot.send_message(message.chat.id, 'Привет!✌\nЯ, возможно, смогу помочь тебе чем-нибудь.\n'
                                      'Чтобы увидить список доступных комманд, нажми сюда👇', reply_markup=HelpInline)
                                        #TODO спрятать весь текст в переменные
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, ComList, reply_markup=keyboard1)

@bot.callback_query_handler(func=lambda c: c.data == 'help')
def process_callback_help(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, ComList, reply_markup=keyboard1)

@bot.message_handler(commands=['PrevPage']) #TODO объединить в одну функцию с выбором
def message_prev(message):
    bot.send_message(message.chat.id, "Предыдущая страница с командами", reply_markup=keyboard1)
@bot.message_handler(commands=['NextPage'])
def message_page(message):
    bot.send_message(message.chat.id, "Cледующая страница с сообщениями", reply_markup=keyboard2)
@bot.message_handler(commands=['TeleMTUCI'])
def message_tele(message):
    bot.send_message(message.chat.id, 'Вот ваша ссылка на телеграм МТУСИ:\ntg://resolve?domain=mtuci_live')
@bot.message_handler(commands=['InstMTUCI'])
def message_inst(message):
    bot.send_message(message.chat.id, 'Вот ваша ссылка на инстаграм МТУСИ:\nhttps://www.instagram.com/mtuci.official/')
@bot.message_handler(commands=['VkMTUCI'])
def message_vk(message):
    bot.send_message(message.chat.id, 'Вот ваша ссылка на вконтакте МТУСИ:\nhttps://vk.com/mtuci/')

@bot.message_handler(content_types=['text'])
def answer(message):
    query = answers(message)
    answ = query[0]
    key = query[1]
    bot.send_message(message.chat.id, answ, reply_markup=key)
    # bot.send_animation(message.chat.id, animation=open('ezgif-7-49bd7b3d26.gif', 'rb'))

bot.polling(none_stop=True)
