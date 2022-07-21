from Keyboards import *
from bd import answ_bd, Wansw_bd, week_bd

def answers(message):
    key = None
    match message.text.lower():
        case "мтуси🔎":
            answer = "Хочешь узнать свежую информацию о МТУСИ?\nТогда тебе сюда – https://mtuci.ru/"
        case "пошли гулять":
            answer = "Я робот, но он может погулять вместо меня:\nhttps://vk.com/the_best_0ne"
        case "выключи свет":
            answer = "Ага, а чай тебе не сделать? Совсем офигел"
        case "хочу спать":
            answer = "Ну молодец, я не знаю что такое спать, я робот. Но вот это, возможно, тебе поможет:"\
                    "\nhttps://nukadeti.ru/skazki"
        case "скажи мой id":
            answer = 'Вот твой id ' + str(message.chat.id)
        case "следующая страница👉":
            answer = "Cледующая страница с сообщениями"
            key = keyboard2
        case "👈предыдущая страница":
            answer = "Предыдущая страница с командами"
            key = keyboard1
        case "помощь😿":
            answer = ComList
            key = keyboard1
        case "мтуси💌":
            answer = "Вот ваша ссылка на телеграм МТУСИ:\ntg://resolve?domain=mtuci_live"
        case "мтуси📺":
            answer = "Вот ваша ссылка на инстаграм МТУСИ:\nhttps://www.instagram.com/mtuci.official/"
        case "мтуси👥":
            answer = "Вот ваша ссылка на вконтакте МТУСИ:\nhttps://vk.com/mtuci/"
        case "справка📄":
            answer = "Выберете что бы вы хотели узнать:"
            key = keyboard_link
        case "начать💎": #TODO дать предназночение боту
            answer = "Веберете какое расписание вы хотите:"
            key = keyboard_rasp
        case "инст📺":
            answer = "Вот инстагар моего хозяина: https://www.instagram.com/quangomgp/"
        case "вк👥":
            answer = "Вот ВК моего хозяина: https://vk.com/the_best_0ne"
        case "github💾":
            answer = "Вот Github моего хозяина: https://github.com/QuangoMGP \n" \
                     "Но первая версия меня лежит тут: https://gist.github.com/QuangoMGP"
        case "о проекте⚙":
            answer = "В разработке!"#TODO когда доделаю бота, нужно рассказать о проекте
        case "в начало🏠":
            answer = "Переход в самое начало"
            key = keyboard1
        case "понедельник🏞":
            answer =answ_bd(1)
            key = Backtorasp
        case "вторник🌅":
            answer = answ_bd(2)
            key = Backtorasp
        case "среда🌄":
            answer = answ_bd(3)
            key = Backtorasp
        case "четверг🌠":
            answer = answ_bd(4)
            key = Backtorasp
        case "пятница🎇":
            answer = answ_bd(5)
            key = Backtorasp
        case "суббота🎆":
            answer = answ_bd(6)
            key = Backtorasp
        case "текущая неделя":
            answer = Wansw_bd(0)
            key = Backtorasp
        case "следующая неделя":
            answer = Wansw_bd(1)
            key = Backtorasp
        case "неделя🗓":
            answer = week_bd()
            key = Backtorasp


        # Можно добавить свои ответы на фразы:
        #
        # case "фраза на которую бот будет реагировать":
        #     answer = "его ответ на вашу фразу"
        #     если нужна клавиатура то пишем:
        #     key = КЛАВИАТУРА

        case _:
            answer = 'Я вас не понимаю, чтобы увидеть список комманд введите /help'
    return [answer, key]

#TODO Изменить Help в конце
ComList = "Я умею: \n" \
      "\nВыводить команды:" \
      "\n  /help - список доступных действий" \
      "\n  /TeleMTUCI - отправляет ссылку на телеграм МТУСИ" \
      "\n  /InstMTUCI - отправляет ссылку на инстаграм МТУСИ" \
      "\n  /VkMTUCI - отправляет ссылку на вконтакте МТУСИ" \
      "\nОтвечать на сообщения:" \
      "\n  -МТУСИ - оффициальный сайт МТУСИ" \
      "\n  -Хочу спать - помогает уснуть" \
      "\n  -Пошли гулять - говорит кого можно позвать" \
      "\n  -Выключи свет - должен выключать свет" \
      "\n  -Cкажи мой id - отправляет ваш id"
