import telebot
from telebot import types
import psycopg2
from config import host, user, password, db_name
import os
from flask import Flask, request


TOKEN = '2083903747:AAGTeoLnDe5c-IybyKoVZMRJKli5CCd2AX0'
APP_URL = f'https://botstiralka.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


# connect to exist database
connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name    
    )
connection.autocommit = True
    
    # the cursor for perfoming database operations
    # cursor = connection.cursor()
def db_table_val(machine_id: str, machine_status: str):
    connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO machine (machine_id, machine_status) VALUES (?, ?)', (machine_id, machine_status)
    )


@bot.message_handler(commands=['start'])
def start(message):
    rmk = types.ReplyKeyboardMarkup()
    rmk.add(types.KeyboardButton('Машинка 1'), types.KeyboardButton('Машинка 2'), types.KeyboardButton('Машинка 3'), types.KeyboardButton('Машинка 4'))
    
    msg = bot.send_message(message.chat.id, 'Привет, {0.first_name}, выбери номер машинки.'.format(message.from_user), reply_markup=rmk)
    bot.register_next_step_handler(msg, user_answer)
    
def user_answer(message):
    rmk1 = types.ReplyKeyboardMarkup()
    rmk1.add(types.KeyboardButton('45'), types.KeyboardButton('60'))
    
    if message.text == 'Машинка 1':
        msg = bot.send_message(message.chat.id, 'Машинка 1. Выбери температурный режим', reply_markup=rmk1)
        bot.register_next_step_handler(msg, mode_machine)
        
        #ЗАПИСЬ В БД
        mach_id = 1
        mach_stat = 0
        db_table_val(machine_id=mach_id, machine_status=mach_stat)
        
    elif message.text == 'Машинка 2':
        msg = bot.send_message(message.chat.id, 'Машинка 2. Выбери температурный режим', reply_markup=rmk1)
        bot.register_next_step_handler(msg, mode_machine)
        
        #ЗАПИСЬ В БД
        mach_id = 2
        mach_stat = 0
        db_table_val(machine_id=mach_id, machine_status=mach_stat)
        
        
    elif message.text == 'Машинка 3':
        msg = bot.send_message(message.chat.id, 'Машинка 3. Выбери температурный режим', reply_markup=rmk1)
        bot.register_next_step_handler(msg, mode_machine)
        #ЗАПИСЬ В БД
        mach_id = 3
        mach_stat = 0
        db_table_val(machine_id=mach_id, machine_status=mach_stat)
        
    elif message.text == 'Машинка 4':
        msg = bot.send_message(message.chat.id, 'Машинка 4. Выбери температурный режим', reply_markup=rmk1)
        bot.register_next_step_handler(msg, mode_machine)
        #ЗАПИСЬ В БД
        mach_id = 1
        mach_stat = 0
        db_table_val(machine_id=mach_id, machine_status=mach_stat)
       
        

def mode_machine(message):
    rmk2 = types.ReplyKeyboardMarkup()
    rmk2.add(types.KeyboardButton('Начать стирку'))
    
    if message.text == '45':
        msg = bot.send_message(message.chat.id, 'Закрой машинку и начни стирку', reply_markup=rmk2)
        bot.register_next_step_handler(msg, change_status)
    elif message.text == '60':
        msg = bot.send_message(message.chat.id, 'Закрой машинку и начни стирку', reply_markup=rmk2)
        bot.register_next_step_handler(msg, change_status)

def change_status(message):
    rmk3 = types.ReplyKeyboardMarkup()
    rmk3.add(types.KeyboardButton('Открыть машинку'))
    bot.send_message(message.chat.id, 'Стирка окончена, открой машинку!', reply_markup=rmk3)


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))