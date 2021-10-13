import telebot
from telebot import types
import sqlite3


client = telebot.TeleBot('2083903747:AAGTeoLnDe5c-IybyKoVZMRJKli5CCd2AX0');
bot_url= 'https://git.heroku.com/botstirka.git'

conn = sqlite3.connect('K:\SQL Lite\BotDB.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, user_name: str, machine_id: str, machine_status: str):
	cursor.execute('INSERT INTO General (user_id, user_name, machine_id, machine_status) VALUES (?, ?, ?, ?)', (user_id, user_name, machine_id, machine_status))
	conn.commit()


@client.message_handler(commands=['start'])
def start(message):
    rmk = types.ReplyKeyboardMarkup()
    rmk.add(types.KeyboardButton('Машинка 1'), types.KeyboardButton('Машинка 2'), types.KeyboardButton('Машинка 3'), types.KeyboardButton('Машинка 4'))
    
    msg = client.send_message(message.chat.id, 'Привет, {0.first_name}, выбери номер машинки.'.format(message.from_user), reply_markup=rmk)
    client.register_next_step_handler(msg, user_answer)
    
def user_answer(message):
    rmk1 = types.ReplyKeyboardMarkup()
    rmk1.add(types.KeyboardButton('45'), types.KeyboardButton('60'))
    
    if message.text == 'Машинка 1':
        msg = client.send_message(message.chat.id, 'Машинка 1. Выбери температурный режим', reply_markup=rmk1)
        client.register_next_step_handler(msg, mode_machine)
        
        #ЗАПИСЬ В БД
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        mach_id = 1
        mach_stat = 0
        db_table_val(user_id=us_id, user_name=us_name, machine_id=mach_id, machine_status=mach_stat)
        
    elif message.text == 'Машинка 2':
        msg = client.send_message(message.chat.id, 'Машинка 2. Выбери температурный режим', reply_markup=rmk1)
        client.register_next_step_handler(msg, mode_machine)
        
        #ЗАПИСЬ В БД
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        mach_id = 2
        mach_stat = 0
        db_table_val(user_id=us_id, user_name=us_name, machine_id=mach_id, machine_status=mach_stat)
        
    elif message.text == 'Машинка 3':
        msg = client.send_message(message.chat.id, 'Машинка 3. Выбери температурный режим', reply_markup=rmk1)
        client.register_next_step_handler(msg, mode_machine)
        
        #ЗАПИСЬ В БД
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        mach_id = 3
        mach_stat = 0
        db_table_val(user_id=us_id, user_name=us_name, machine_id=mach_id, machine_status=mach_stat)
        
    elif message.text == 'Машинка 4':
        msg = client.send_message(message.chat.id, 'Машинка 4. Выбери температурный режим', reply_markup=rmk1)
        client.register_next_step_handler(msg, mode_machine)
        
        #ЗАПИСЬ В БД
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        mach_id = 4
        mach_stat = 0
        db_table_val(user_id=us_id, user_name=us_name, machine_id=mach_id, machine_status=mach_stat)
        

def mode_machine(message):
    rmk2 = types.ReplyKeyboardMarkup()
    rmk2.add(types.KeyboardButton('Начать стирку'))
    
    if message.text == '45':
        msg = client.send_message(message.chat.id, 'Закрой машинку и начни стирку', reply_markup=rmk2)
        client.register_next_step_handler(msg, change_status, set_timer)
    elif message.text == '60':
        msg = client.send_message(message.chat.id, 'Закрой машинку и начни стирку', reply_markup=rmk2)
        client.register_next_step_handler(msg, change_status, set_timer)

def change_status(message):
    rmk3 = types.ReplyKeyboardMarkup()
    rmk3.add(types.KeyboardButton('Открыть машинку'))
    client.send_message(message.chat.id, 'Стирка окончена, открой машинку!', reply_markup=rmk3)
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    mach_id = 2
    mach_stat = 1
    db_table_val(user_id=us_id, user_name=us_name, machine_id=mach_id, machine_status=mach_stat)

#ТАЙМЕР
def task(bot, job):
    bot.send_message(job.context, text='Стирка окончена, открой машинку!')

def set_timer(bot, update, job_queue, chat_data):
    
    # создаём задачу task в очереди job_queue
    # передаём ей идентификатор текущего чата
    # идентификатор далее будет доступен через job.context
    
    delay = 5 # количество секунд
    job = job_queue.run_once(task, delay, context=update.message.chat_id)

    # Регистрируем созданную задачу в пользовательских данных
    chat_data['job'] = job
    
    # Сообщаем о том, что таймер установлен
    client.send_message('Таймер установлен на ' + str(delay) + ' секунд' )

        
client.polling()
        