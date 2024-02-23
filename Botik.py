import telebot
from telebot import types
import pymysql
from config import host, user, password, db_name
from datetime import date, timedelta
bot = telebot.TeleBot('6989942925:AAHi9jq8P3iw5zQc2lBF7b7ggNU85JlYXLk')
NowDat = ''

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, напиши интересующую тебя дату в формате гггг-мм-дд, например 2024-01-01')
    bot.register_next_step_handler(message, new_days)

@bot.message_handler(commands=['back'])
def main(message):
    bot.send_message(message.chat.id, 'Напиши интересующую тебя дату в формате гггг-мм-дд, например 2024-01-01')
    bot.register_next_step_handler(message, new_days)


def new_days(message):
    global NowDat
    try:
        connection = pymysql.connect(
            host = host,
            port = 3306,
            user = user,
            password = password,
            database = db_name
        )
        connection.autocommit = True
        cur = connection.cursor()

        NowDat = message.text
        NowDat = date.fromisoformat(NowDat)         ###Полученная дата 
        NowDat = "'" + str(NowDat) + "'"
        days = '1'
        delt = timedelta(days=int(days))
        lastDatT = "'" + str(date.today()) + "'"
        cur.execute(f'INSERT INTO schedule (data) VALUES ({lastDatT}) ON CONFLICT DO NOTHING;')
        lastDatI = date.today()

        for i in range(13):
            lastDatI += delt
            lastDatT = "'" + str(lastDatI) + "'"
            cur.execute(f'INSERT INTO schedule (data) VALUES ({lastDatT}) ON CONFLICT DO NOTHING;')
                

        todayDat = "'" + str(date.today()) + "'"
        cur.execute(f'SELECT data_id FROM schedule WHERE data={todayDat}')
        todayID = cur.fetchone()
        todayID = int(todayID[0])
        cur.execute(f'DELETE FROM schedule WHERE data_id < {todayID}')
        

        cur.execute(f'SELECT * FROM schedule where data={NowDat}')
        schedule = cur.fetchall()
        table = f'  Расписание актового зала на \n                {NowDat}  \n\n'
        table1 = table
        markup = types.InlineKeyboardMarkup(row_width=2)

        for el in schedule: 
            if el[2]==0 and el[3]==0:
                table+=(f'1 урок  - свободен\n\n')
                table+=(f'1 перемена - свободна\n\n')
                btn1 = types.InlineKeyboardButton("1 урок", callback_data='zan1')
                btn2 = types.InlineKeyboardButton("1 перемена", callback_data='zan2')
                markup.row(btn1, btn2)
            else:
                if el[2]==0:
                    table+=(f'1 урок  - свободен\n\n')
                    btn1 = types.InlineKeyboardButton("1 урок", callback_data='zan1')
                    markup.add(btn1)
                elif el[2]==1:
                    table+=(f'1 урок - занят\n\n')
            
                if el[3]==0:
                    table+=(f'1 перемена - свободна\n\n')
                    btn2 = types.InlineKeyboardButton("1 перемена", callback_data='zan2')
                    markup.add(btn2)
                elif el[3]==1:
                    table+=(f'1 перемена - занята\n\n')

            if el[4]==0 and el[5]==0:
                table+=(f'2 урок - свободен\n\n')
                btn3 = types.InlineKeyboardButton("2 урок", callback_data='zan3')
                table+=(f'2 перемена - свободна\n\n')
                btn4 = types.InlineKeyboardButton("2 перемена", callback_data='zan4')
                markup.row(btn3, btn4)
            else:
                if el[4]==0:
                    table+=(f'2 урок - свободен\n\n')
                    btn3 = types.InlineKeyboardButton("2 урок", callback_data='zan3')
                    markup.add(btn3)
                elif el[4]==1:
                    table+=(f'2 урок - занят\n\n')
        
                if el[5]==0:
                    table+=(f'2 перемена - свободна\n\n')
                    btn4 = types.InlineKeyboardButton("2 перемена", callback_data='zan4')
                    markup.add(btn4)
                elif el[5]==1:
                    table+=(f'2 перемена - занята\n\n')
            
            if el[6]==0 and el[7]==0:
                table+=(f'3 урок - свободен\n\n')
                btn5 = types.InlineKeyboardButton("3 урок", callback_data='zan5')
                table+=(f'3 перемена - свободна\n\n')
                btn6 = types.InlineKeyboardButton("3 перемена", callback_data='zan6')
                markup.row(btn5, btn6)
            else:
                if el[6]==0:
                    table+=(f'3 урок - свободен\n\n')
                    btn5 = types.InlineKeyboardButton("3 урок", callback_data='zan5')
                    markup.add(btn5)
                elif el[6]==1:
                    table+=(f'3 урок - занят\n\n')
            
        
                if el[7]==0:
                    table+=(f'3 перемена - свободна\n\n')
                    btn6 = types.InlineKeyboardButton("3 перемена", callback_data='zan6')
                    markup.add(btn6)
                elif el[7]==1:
                    table+=(f'3 перемена - занята\n\n')
            
            if el[8]==0 and el[9]==0:
                table+=(f'4 урок - свободен\n\n')
                btn7 = types.InlineKeyboardButton("4 урок", callback_data='zan7')
                table+=(f'4 перемена - свободна\n\n')
                btn8 = types.InlineKeyboardButton("4 перемена", callback_data='zan8')
                markup.row(btn7, btn8)
            else:
                if el[8]==0:
                    table+=(f'4 урок - свободен\n\n')
                    btn7 = types.InlineKeyboardButton("4 урок", callback_data='zan7')
                    markup.add(btn7)
                elif el[8]==1:
                    table+=(f'4 урок - занят\n\n')
            
        
                if el[9]==0:
                    table+=(f'4 перемена - свободна\n\n')
                    btn8 = types.InlineKeyboardButton("4 перемена", callback_data='zan8')
                    markup.add(btn8)
                elif el[9]==1:
                    table+=(f'4 перемена - занята\n\n')
            
            if el[10]==0 and el[11]==0:
                table+=(f'5 урок - свободен\n\n')
                btn9 = types.InlineKeyboardButton("5 урок", callback_data='zan9')
                table+=(f'5 перемена - свободна\n\n')
                btn10 = types.InlineKeyboardButton("5 перемена", callback_data='zan10')
                markup.row(btn9, btn10)
            else:
                if el[10]==0:
                    table+=(f'5 урок - свободен\n\n')
                    btn9 = types.InlineKeyboardButton("5 урок", callback_data='zan9')
                    markup.add(btn9)
                elif el[10]==1:
                    table+=(f'5 урок - занят\n\n')
            
        
                if el[11]==0:
                    table+=(f'5 перемена - свободна\n\n')
                    btn10 = types.InlineKeyboardButton("5 перемена", callback_data='zan10')
                    markup.add(btn10)
                elif el[11]==1:
                    table+=(f'5 перемена - занята\n\n')
            
            if el[12]==0 and el[13]==0:
                table+=(f'6 урок - свободен\n\n')
                btn11 = types.InlineKeyboardButton("6 урок", callback_data='zan11')
                table+=(f'6 перемена - свободна\n\n')
                btn12 = types.InlineKeyboardButton("6 перемена", callback_data='zan12')
                markup.row(btn11, btn12)
            else:
                if el[12]==0:
                    table+=(f'6 урок - свободен\n\n')
                    btn11 = types.InlineKeyboardButton("6 урок", callback_data='zan11')
                    markup.add(btn11)
                elif el[12]==1:
                    table+=(f'6 урок - занят\n\n')
            
        
                if el[13]==0:
                    table+=(f'6 перемена - свободна\n\n')
                    btn12 = types.InlineKeyboardButton("6 перемена", callback_data='zan12')
                    markup.add(btn12)
                elif el[13]==1:
                    table+=(f'6 перемена - занята\n\n')
            
            if el[14]==0 and el[15]==0:
                table+=(f'7 урок - свободен\n\n')
                btn13 = types.InlineKeyboardButton("7 урок", callback_data='zan13')
                table+=(f'7 перемена - свободна\n\n')
                btn14 = types.InlineKeyboardButton("7 перемена", callback_data='zan14')
                markup.row(btn13, btn14)
            else:
                if el[14]==0:
                    table+=(f'7 урок - свободен\n\n')
                    btn13 = types.InlineKeyboardButton("7 урок", callback_data='zan13')
                    markup.add(btn13)
                elif el[14]==1:
                    table+=(f'7 урок - занят\n\n')
            
        
                if el[15]==0:
                    table+=(f'7 перемена - свободна\n\n')
                    btn14 = types.InlineKeyboardButton("7 перемена", callback_data='zan14')
                    markup.add(btn14)
                elif el[15]==1:
                    table+=(f'7 перемена - занята\n\n')
            

            if el[16]==0:
                table+=(f'8 урок - свободен\n\n')
                btn15 = types.InlineKeyboardButton("8 урок", callback_data='zan15')
                markup.add(btn15)
            elif el[16]==1:
                table+=(f'8 урок - занят\n\n')
        if table == table1:
            table += 'К сожалению, на данную дату расписания нет!'
        bot.send_message(message.chat.id, table, reply_markup=markup)
        table = ''

                  

    except Exception as _ex:
        print('[INFO] Error while working with MySQL', _ex)
    finally:
        if connection:
            cur.close()
            connection.close()
            print("[INFO] MySQL connection closed")



@bot.callback_query_handler(func = lambda callback:callback)
def zana(callback):
    try:
        connection = pymysql.connect(
            host = host,
            port = 3306,
            user = user,
            password = password,
            database = db_name
        )
        cur = connection.cursor()
        connection.autocommit = True

        if callback.data == 'zan1':
            cur.execute(f'UPDATE schedule SET lsn1 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 1 урок на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan2':
            cur.execute(f'UPDATE schedule SET brk1 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 1 перемену на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan3':
            cur.execute(f'UPDATE schedule SET lsn2 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 2 урок на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan4':
            cur.execute(f'UPDATE schedule SET brk2 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 2 перемену на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan5':
            cur.execute(f'UPDATE schedule SET lsn3 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 3 урок на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan6':
            cur.execute(f'UPDATE schedule SET brk3 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 3 перемену на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan7':
            cur.execute(f'UPDATE schedule SET lsn4 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 4 урок на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan8':
            cur.execute(f'UPDATE schedule SET brk4 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 4 перемену на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan9':
            cur.execute(f'UPDATE schedule SET lsn5 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 5 урок на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan10':
            cur.execute(f'UPDATE schedule SET brk5 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 5 перемену на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan11':
            cur.execute(f'UPDATE schedule SET lsn6 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 6 урок на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan12':
            cur.execute(f'UPDATE schedule SET brk6 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 6 перемену на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan13':
            cur.execute(f'UPDATE schedule SET lsn7 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 7 урок на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan14':
            cur.execute(f'UPDATE schedule SET brk7 = 1 WHERE data = {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 7 перемену на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')
        elif callback.data == 'zan15':
            cur.execute(f'UPDATE schedule SET lsn8 = 1 WHERE data =  {NowDat}')
            bot.send_message( callback.message.chat.id, f'Отично, вы успешно заняли 8 урок на {NowDat}\n чтобы вернуться к выбору даты, напишите "/back"')

    except Exception as _ex:
        print('[INFO] Error while working with MySQL', _ex)
    finally:
        if connection:
            cur.close()
            connection.close()
            print("[INFO] MySQL connection closed")
            





bot.infinity_polling()