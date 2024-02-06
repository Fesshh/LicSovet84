import telebot
import sqlite3
from telebot import types
bot = telebot.TeleBot('6989942925:AAHi9jq8P3iw5zQc2lBF7b7ggNU85JlYXLk')

@bot.message_handler(commands=['start']):
def main(message):
    bot.send_message(message.chat.id, 'Привет, напиши интересующую тебя дату. Например: 01.01.2024')