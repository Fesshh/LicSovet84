import telebot
import sqlite3
from telebot import types
from datetime import date, timedelta
bot = telebot.TeleBot('6989942925:AAHi9jq8P3iw5zQc2lBF7b7ggNU85JlYXLk')

@bot.message_handler(commands=['start'])
def main(message):
    conn = sqlite3.connect('LicSov84.sql')
    cur = conn.cursor()
    dat1 = date.fromisoformat('2024-01-01')             ###Первая дата в таблице 

    cur.execute('CREATE TABLE IF NOT EXISTS schedule (id int auto_increment primay key, datt date NOT NULL, lsn1 int DEFAULT 0 , brk1 int DEFAULT 0, lsn2 int DEFAULT 0, brk2 int DEFAULT 0, lsn3 int DEFAULT 0, brk3 int DEFAULT 0, lsn4 int DEFAULT 0, brk4 int DEFAULT 0, lsn5 int DEFAULT 0, brk5 int DEFAULT 0, lsn6 int DEFAULT 0, brk6 int DEFAULT 0, lsn7 int DEFAULT 0, brk7 int DEFAULT 0, lsn8 int DEFAULT 0)')
    cur.execute(f'INSERT IF NOT EXISTS INTO schedule (datt) VALUES({dat1})')

    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Привет, напиши интересующую тебя дату в формате гггг-мм-дд, например 2024-01-01')
    bot.register_next_step_handler(message, new_days)


def new_days(message):
    conn = sqlite3.connect('LicSov84.sql')
    cur = conn.cursor()
    NowDat = message.tetx()
    NowDat = date.fromisoformat(NowDat)         ###Полученная дата  
    lastDat = cur.execute('SELESCT MAX(id) FROM schedule')  ###Последняя дата в таблице 
    todayDat = date.today()                    ###Сегодняшняя дата
    todayDat+=14
    days = '1'
    delt = timedelta(days=int(days))
    todayID = cur.execute(f'SELECT id FROM schedule WHERE datt={todayDat}')

    while lastDat<todayDat:
        lastDat += delt
        cur.execute(f'INSERT INTO schedule (datt) VALUES({lastDat})')

    cur.execute(f'DELETE FROM schedule WHERE id < {todayID}')

    cur.execute(f'SELESECT * FROM schedule where datt={NowDat}')
    schedule = cur.fetchall()
    table = ''

    for el in schedule:
        if el[2]==0:
            table+=(f'1ый урок свободен\n')
        elif el[2]==1:
            table+=(f'1ый урок занят\n')

        if el[3]==0:
            table+=(f'1ая перемена свободна\n')
        elif el[3]==1:
            table+=(f'1ая перемена занята\n')

        if el[3]==0:
            table+=(f'2ой урок свободен\n')
        elif el[3]==1:
            table+=(f'2ой урок занят\n')
        
        if el[4]==0:
            table+=(f'2ая перемена свободна\n')
        elif el[4]==1:
            table+=(f'2ая перемена занята\n')
            
        
        if el[5]==0:
            table+=(f'3ий урок свободен\n')
        elif el[5]==1:
            table+=(f'3ий урок занят\n')
            
        
        if el[6]==0:
            table+=(f'3ья перемена свободна\n')
        elif el[6]==1:
            table+=(f'3ья перемена занята\n')
            
        
        if el[7]==0:
            table+=(f'4ый урок свободен\n')
        elif el[7]==1:
            table+=(f'4ый урок занят\n')
            
        
        if el[8]==0:
            table+=(f'4ая перемена свободна\n')
        elif el[8]==1:
            table+=(f'4ая перемена занята\n')
            
        
        if el[9]==0:
            table+=(f'5ый урок свободен\n')
        elif el[9]==1:
            table+=(f'5ый урок занят\n')
            
        
        if el[10]==0:
            table+=(f'5ая перемена свободна\n')
        elif el[10]==1:
            table+=(f'5ая перемена занята\n')
            
        
        if el[11]==0:
            table+=(f'6ый урок свободен\n')
        elif el[11]==1:
            table+=(f'6ый урок занят\n')
            
        
        if el[12]==0:
            table+=(f'6ая перемена свободна\n')
        elif el[12]==1:
            table+=(f'6ая перемена занята\n')
            
        
        if el[13]==0:
            table+=(f'7ой урок свободен\n')
        elif el[13]==1:
            table+=(f'7ой урок занят\n')
            
        
        if el[14]==0:
            table+=(f'7ая перемена свободна\n')
        elif el[14]==1:
            table+=(f'7ая перемена занята\n')
            
        
        if el[15]==0:
            table+=(f'8ой урок свободен\n')
        elif el[15]==1:
            table+=(f'8ой урок занят\n')


    bot.send_message(message, table)
         
        
            
        

        

###17


    





    
    
    
    
    
    conn.commit()
    cur.close()
    conn.close()

bot.infinity_polling()