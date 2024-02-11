import telebot
from telebot import types
import psycopg2
from config import host, user, password, db_name
from datetime import date, timedelta, datetime
bot = telebot.TeleBot('6989942925:AAHi9jq8P3iw5zQc2lBF7b7ggNU85JlYXLk')

def check_today(conn, table, data1):
    cursor = conn. cursor()
    query = "SELECT EXISTS(SELECT 1 FROM %s WHERE data = %s)"
    values = (table, data1)
    cursor.execute(query, values)
    row = cursor.fetchone()
    return bool(row[0])

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, напиши интересующую тебя дату в формате гггг-мм-дд, например 2024-01-01')
    bot.register_next_step_handler(message, new_days)


def new_days(message):
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        connection.autocommit = True
        cur = connection.cursor()

        NowDat = message.text
        print(NowDat)
        NowDat = date.fromisoformat(NowDat)         ###Полученная дата  
        lastDat = cur.execute('SELECT MAX(data_id) FROM schedule')  ###Последняя дата в таблице 
        todayDat = '"' + str(date.today()) + '"'                   ###Сегодняшняя дата
        cur.execute(f'SELECT EXISTS(SELECT 1 FROM schedule WHERE data = {todayDat} )')
        davno = cur.fetchone()
        davno = bool(davno)
        print(davno)
        print(1)
        todayDat = date.fromisoformat(todayDat)
        days = '14'
        delt = timedelta(days=int(days))
        todayDat+=delt
        days = '1'
        delt = timedelta(days=int(days))
        lastDat = date.fromisoformat(lastDat)
        


        if davno == True:
            while lastDat<todayDat:
                lastDat += delt
                cur.execute(f'INSERT INTO schedule (data) VALUES({lastDat})')
        else:
            for i in range(14):
                lastDat = date.today()
                cur.execute(f'INSERT INTO schedule (data) VALUES({lastDat})')
                lastDat += delt

        todayDat = '"' + str(todayDat) + '"'
        todayID = cur.execute(f'SELECT data_id FROM schedule WHERE data={todayDat}')
        cur.execute(f'DELETE FROM schedule WHERE data_id < {todayID}')
        

        cur.execute(f'SELECT * FROM schedule where data={NowDat}')
        schedule = cur.fetchall()
        table = ''
        odin = 1
        markup = types.InlineKeyboardMarkup()

        for el in schedule:
            if el[2]==0:
                table+=(f'1ый урок свободен\n')
                btn1 = types.InlineKeyboardButton("1ый урок", callback_data='zan1')
                markup.add(btn1)
            elif el[2]==1:
                table+=(f'1ый урок занят\n')

            if el[3]==0:
                table+=(f'1ая перемена свободна\n')
                btn2 = types.InlineKeyboardButton("1ая перемена", callback_data='zan2')
                markup.add(btn2)
            elif el[3]==1:
                table+=(f'1ая перемена занята\n')

            if el[3]==0:
                table+=(f'2ой урок свободен\n')
                btn3 = types.InlineKeyboardButton("2ой урок", callback_data='zan3')
                markup.add(btn3)
            elif el[3]==1:
                table+=(f'2ой урок занят\n')
        
            if el[4]==0:
                table+=(f'2ая перемена свободна\n')
                btn4 = types.InlineKeyboardButton("2ая перемена", callback_data='zan4')
                markup.add(btn4)
            elif el[4]==1:
                table+=(f'2ая перемена занята\n')
            
        
            if el[5]==0:
                table+=(f'3ий урок свободен\n')
                btn5 = types.InlineKeyboardButton("3ий урок", callback_data='zan5')
                markup.add(btn5)
            elif el[5]==1:
                table+=(f'3ий урок занят\n')
            
        
            if el[6]==0:
                table+=(f'3ья перемена свободна\n')
                btn6 = types.InlineKeyboardButton("3ья перемена", callback_data='zan6')
                markup.add(btn6)
            elif el[6]==1:
                table+=(f'3ья перемена занята\n')
            
        
            if el[7]==0:
                table+=(f'4ый урок свободен\n')
                btn7 = types.InlineKeyboardButton("4ый урок", callback_data='zan7')
                markup.add(btn7)
            elif el[7]==1:
                table+=(f'4ый урок занят\n')
            
        
            if el[8]==0:
                table+=(f'4ая перемена свободна\n')
                btn8 = types.InlineKeyboardButton("4ая перемена", callback_data='zan8')
                markup.add(btn8)
            elif el[8]==1:
                table+=(f'4ая перемена занята\n')
            
        
            if el[9]==0:
                table+=(f'5ый урок свободен\n')
                btn9 = types.InlineKeyboardButton("5ый урок", callback_data='zan9')
                markup.add(btn9)
            elif el[9]==1:
                table+=(f'5ый урок занят\n')
            
        
            if el[10]==0:
                table+=(f'5ая перемена свободна\n')
                btn10 = types.InlineKeyboardButton("5ая перемена", callback_data='zan10')
                markup.add(btn10)
            elif el[10]==1:
                table+=(f'5ая перемена занята\n')
            
        
            if el[11]==0:
                table+=(f'6ый урок свободен\n')
                btn11 = types.InlineKeyboardButton("6ый урок", callback_data='zan11')
                markup.add(btn11)
            elif el[11]==1:
                table+=(f'6ый урок занят\n')
            
        
            if el[12]==0:
                table+=(f'6ая перемена свободна\n')
                btn12 = types.InlineKeyboardButton("6ая перемена", callback_data='zan12')
                markup.add(btn12)
            elif el[12]==1:
                table+=(f'6ая перемена занята\n')
            
        
            if el[13]==0:
                table+=(f'7ой урок свободен\n')
                btn13 = types.InlineKeyboardButton("7ой урок", callback_data='zan13')
                markup.add(btn13)
            elif el[13]==1:
                table+=(f'7ой урок занят\n')
            
        
            if el[14]==0:
                table+=(f'7ая перемена свободна\n')
                btn14 = types.InlineKeyboardButton("7ая перемена", callback_data='zan14')
                markup.add(btn14)
            elif el[14]==1:
                table+=(f'7ая перемена занята\n')
            
        
            if el[15]==0:
                table+=(f'8ой урок свободен\n')
                btn15 = types.InlineKeyboardButton("8ой урок", callback_data='zan15')
                markup.add(btn15)
            elif el[15]==1:
                table+=(f'8ой урок занят\n')
        
        bot.send_message(message, table, reply_markup=markup)
        table = ''

                  

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cur.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")



@bot.callback_query_handler(func = lambda callback:callback)
def zana(callback):
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        cur = connection.cursor()
        odin = 1

        if callback.data == 'zan1':
            cur.execute(f'UPDATE schedule SET lsn1 = {odin}')
        elif callback.data == 'zan2':
            cur.execute(f'UPDATE schedule SET brk1 = {odin}')
        elif callback.data == 'zan3':
            cur.execute(f'UPDATE schedule SET lsn2 = {odin}')
        elif callback.data == 'zan4':
            cur.execute(f'UPDATE schedule SET brk2 = {odin}')
        elif callback.data == 'zan5':
            cur.execute(f'UPDATE schedule SET lsn3 = {odin}')
        elif callback.data == 'zan6':
            cur.execute(f'UPDATE schedule SET brk3 = {odin}')
        elif callback.data == 'zan7':
            cur.execute(f'UPDATE schedule SET lsn4 = {odin}')
        elif callback.data == 'zan8':
            cur.execute(f'UPDATE schedule SET brk4 = {odin}')
        elif callback.data == 'zan9':
            cur.execute(f'UPDATE schedule SET lsn5 = {odin}')
        elif callback.data == 'zan10':
            cur.execute(f'UPDATE schedule SET brk5 = {odin}')
        elif callback.data == 'zan11':
            cur.execute(f'UPDATE schedule SET lsn6 = {odin}')
        elif callback.data == 'zan12':
            cur.execute(f'UPDATE schedule SET brk6 = {odin}')
        elif callback.data == 'zan13':
            cur.execute(f'UPDATE schedule SET lsn7 = {odin}')
        elif callback.data == 'zan14':
            cur.execute(f'UPDATE schedule SET brk7 = {odin}')
        elif callback.data == 'zan15':
            cur.execute(f'UPDATE schedule SET lsn8 = {odin}')

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cur.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")
            





bot.infinity_polling()