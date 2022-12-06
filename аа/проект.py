import telebot 
from telebot import types

bot=telebot.TeleBot('5523541243:AAH_S9G4pobRE849JmFhAI5GyRMEF_9rAUg')

@bot.message_handler(commands=['start'])
def start(message):

    mess=f'<b>Привет, <u>{message.from_user.first_name}</u>, я Бот который поможет тебе с подготовкой к ЕГЭ по Информатике)</b>'

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    resh=types.KeyboardButton('Задачи')
    sp=types.KeyboardButton('Справочник')
    markup.add(resh,sp)

    file=open('AnimatedSticker.tgs','rb')

    bot.send_message(message.chat.id,mess, parse_mode='html',reply_markup=markup)
    bot.send_sticker(message.chat.id,file)

@bot.message_handler(content_types=['text'])
def bot_message(message):

    video10=open('ex 10.mp4','rb')
    video11=open('ex 11.mp4','rb')
    video12=open('ex 12.mp4','rb')
    video13=open('ex 13.mp4','rb')
    video14=open('ex 14.mp4','rb')
    video15=open('ex 15.mp4','rb')
    

    png12=open('12.png','rb')
    png13=open('13.png','rb')
    png14=open('14.png','rb')
    png15=open('15.png','rb')

    answer12=open('answer12.png','rb')
    answer13=open('answer13.png','rb')
    answer14=open('answer14.png','rb')
    answer15=open('answer15.png','rb')

    sp1=open('sp1.png','rb')
    sp2=open('sp2.png','rb')
    sp3=open('sp3.png','rb')
    sp41=open('sp4.1.png','rb')
    sp42=open('sp4.2.png','rb')
    sp5=open('sp5.png','rb')
    sp6=open('sp6.png','rb')
    sp7=open('sp7.png','rb')

    doc10=open('10_demo.docx','rb')

    mess2=f'<b>С помощью текстового редактора определите, сколько раз, не считая сносок, встречается слово «свет» или «Свет» в тексте романа в стихах А. С. Пушкина «Евгений Онегин». Другие формы слова «свет», такие как «светло», «светает» и т. д., учитывать не следует. В ответе укажите только число.</b>'
    
    if message.text=='Задачи':

        markup1=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        num10=types.KeyboardButton('Номер 1️⃣0️⃣')
        num11=types.KeyboardButton('Номер 1️⃣1️⃣')
        num12=types.KeyboardButton('Номер 1️⃣2️⃣')
        num13=types.KeyboardButton('Номер 1️⃣3️⃣')
        num14=types.KeyboardButton('Номер 1️⃣4️⃣')
        num15=types.KeyboardButton('Номер 1️⃣5️⃣')
        bk=types.KeyboardButton('⏩Назад')

        markup1.add(num10,num11,num12,num13,num14,num15,bk)
        
        bot.send_message(message.chat.id,'<b>Выбери номер, который хочешь разобрать.</b>',parse_mode='html',reply_markup=markup1)

    elif message.text=='Справочник':

        markup2=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        s1=types.KeyboardButton('Формула Хартли')
        s2=types.KeyboardButton('Формула Шеннона')
        s3=types.KeyboardButton('Обозначение кол-в информации')
        s41=types.KeyboardButton('Прямое условие Фано')
        s42=types.KeyboardButton('Обратное условие Фано')
        s5=types.KeyboardButton('Задачи на графах')
        s6=types.KeyboardButton('Системы счисления (теория)')
        s7=types.KeyboardButton('Системы счисления')
        bk=types.KeyboardButton('⏩Назад')
        markup2.add(s1,s2,s3,s41,s42,s5,s6,s7,bk)
        bot.send_message(message.chat.id,'<b>Выбери тему, для справки.</b>',parse_mode='html',reply_markup=markup2)

    elif message.text=='Формула Хартли':
        bot.send_message(message.chat.id,'<b>Держи)</b>',parse_mode='html')
        bot.send_photo(message.chat.id,sp1)

    elif message.text=='Формула Шеннона':
        bot.send_message(message.chat.id,'<b>Держи)</b>',parse_mode='html')
        bot.send_photo(message.chat.id,sp2)

    elif message.text=='Обозначение кол-в информации':
        bot.send_message(message.chat.id,'<b>Держи)</b>',parse_mode='html')
        bot.send_photo(message.chat.id,sp3)

    elif message.text=='Прямое условие Фано':
        bot.send_message(message.chat.id,'<b>Держи)</b>',parse_mode='html')
        bot.send_photo(message.chat.id,sp41)

    elif message.text=='Обратное условие Фано':
        bot.send_message(message.chat.id,'<b>Держи)</b>',parse_mode='html')
        bot.send_photo(message.chat.id,sp42)
    elif message.text=='Задачи на графах':
        bot.send_message(message.chat.id,'<b>Держи)</b>',parse_mode='html')
        bot.send_photo(message.chat.id,sp5)

    elif message.text=='Системы счисления (теория)':
        bot.send_message(message.chat.id,'<b>Держи)</b>',parse_mode='html')
        bot.send_photo(message.chat.id,sp6)

    elif message.text=='Системы счисления':
        bot.send_message(message.chat.id,'<b>Держи)</b>',parse_mode='html')
        bot.send_photo(message.chat.id,sp7)    
    elif message.text=='⏩Назад':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        resh=types.KeyboardButton('Задачи')
        sp=types.KeyboardButton('Справочник')
        markup.add(resh,sp)   

        bot.send_message(message.chat.id,'Выбери <u>Задачи</u> или <u>Справочник</u>', parse_mode='html',reply_markup=markup)
        
    elif message.text=='Номер 1️⃣0️⃣':
        bot.send_message(message.chat.id,'<b>Держи решение)</b>',parse_mode='html')

        action='typing'
        bot.send_chat_action(message.chat.id,action)

        bot.send_video(message.chat.id,video10)

        bot.send_message(message.chat.id,'<b>После просмотра попробуй решить сам</b>',parse_mode='html')
        bot.send_message(message.chat.id,mess2,parse_mode='html')

        bot.send_document(message.chat.id,doc10)

        bot.send_message(message.chat.id,'<b>Псс...</b>',parse_mode='html')

        bot.send_message(message.chat.id,'Правильный ответ: <u>4</u>',parse_mode='html')

    elif message.text=='Номер 1️⃣1️⃣':
        bot.send_message(message.chat.id,'<b>Держи решение)</b>',parse_mode='html')

        action='typing'
        bot.send_chat_action(message.chat.id,action)

        bot.send_video(message.chat.id,video11)

        bot.send_message(message.chat.id,'<b>После просмотра попробуй решить сам</b>',parse_mode='html')
        bot.send_message(message.chat.id,'<b>При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из 10 символов. Для построения идентификатора используют только прописные латинские буквы (26 букв). В базе данных для хранения каждого пароля отведено одинаковое минимально возможное целое число байт. При этом используют посимвольное кодирование паролей, все символы кодируют одинаковым минимально возможным количеством бит. Кроме пароля для каждого пользователя в системе хранятся дополнительные сведения, для чего выделено одинаковое целое количество байт на каждого пользователя. Для хранения информации о 15 пользователях потребовалось 300 байт. Сколько байт выделено для хранения дополнительных сведений об одном пользователе? В ответе запишите только целое число  — количество байт.</b>',parse_mode='html')

        bot.send_message(message.chat.id,'<b>Псс...</b>',parse_mode='html')
        bot.send_message(message.chat.id,'<b>Правильный ответ:</b> <u>13 байт</u>',parse_mode='html')

    elif message.text=='Номер 1️⃣2️⃣':
        bot.send_message(message.chat.id,'<b>Держи решение)</b>',parse_mode='html')

        action='typing'
        bot.send_chat_action(message.chat.id,action)

        bot.send_video(message.chat.id,video12)

        bot.send_message(message.chat.id,'<b>После просмотра попробуй решить сам</b>',parse_mode='html')

        bot.send_photo(message.chat.id,png12)

        bot.send_message(message.chat.id,'<b>Псс...</b>',parse_mode='html')
        bot.send_message(message.chat.id,'<b>Вот решение на питоне:</b>',parse_mode='html')

        bot.send_photo(message.chat.id,answer12)

    elif message.text=='Номер 1️⃣3️⃣':
        bot.send_message(message.chat.id,'<b>Держи решение)</b>',parse_mode='html')

        action='typing'
        bot.send_chat_action(message.chat.id,action)

        bot.send_video(message.chat.id,video13)

        bot.send_message(message.chat.id,'<b>После просмотра попробуй решить сам</b>',parse_mode='html')

        bot.send_photo(message.chat.id,png13)

        bot.send_message(message.chat.id,'<b>Псс...</b>',parse_mode='html')
        bot.send_message(message.chat.id,'<b>Вот решение:</b>',parse_mode='html')

        bot.send_photo(message.chat.id,answer13)

    elif message.text=='Номер 1️⃣4️⃣':
        bot.send_message(message.chat.id,'<b>Держи решение)</b>',parse_mode='html')

        action='typing'
        bot.send_chat_action(message.chat.id,action)

        bot.send_video(message.chat.id,video14)

        bot.send_message(message.chat.id,'<b>После просмотра попробуй решить сам</b>',parse_mode='html')

        bot.send_photo(message.chat.id,png14)

        bot.send_message(message.chat.id,'<b>Псс...</b>',parse_mode='html')
        bot.send_message(message.chat.id,'<b>Вот решение на питоне:</b>',parse_mode='html')

        bot.send_photo(message.chat.id,answer14)

        bot.send_message(message.chat.id,'<u>Ответ: 30</u>',parse_mode='html')

    elif message.text=='Номер 1️⃣5️⃣':
        bot.send_message(message.chat.id,'<b>Держи решение)</b>',parse_mode='html')

        action='typing'
        bot.send_chat_action(message.chat.id,action)

        bot.send_video(message.chat.id,video15)

        bot.send_message(message.chat.id,'<b>После просмотра попробуй решить сам</b>',parse_mode='html')

        bot.send_photo(message.chat.id,png15)

        bot.send_message(message.chat.id,'<b>Псс...</b>',parse_mode='html')
        bot.send_message(message.chat.id,'<b>Вот решение:</b>',parse_mode='html')

        bot.send_photo(message.chat.id,answer15)

bot.polling(none_stop=True)