import telebot
import toml
from telebot import types
import datetime


def load_config(config_name):
    with open(config_name) as f:
        return toml.load(f)


config = load_config(r"D:\python_projects\car_damage_assessment\config.toml")
bot = telebot.TeleBot(config['telegram']['token'])
last_command_code = 0


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Написать админам")
    btn2 = types.KeyboardButton("Оценка повреждений по фото")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот для pet-Проекта с ML, CV и БД".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    global last_command_code
    if last_command_code == 2:
        last_command_code = 0
        print("Получена картинка!")
        bot.send_message(message.chat.id, text="Картинка получена. Хотите сделать что-то ещё?")
        is_answered = False
        is_processed = False
        file_id = message.photo[-1].file_id
        print(f"{message=}")
        # Получение файла
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        print(f"{type(downloaded_file)=}")
        print(f"{len(downloaded_file)=}")
    else:
        bot.send_message(message.chat.id, text="Пожалуйста, сначала выберите 'Оценка повреждений по фото'")


@bot.message_handler(content_types=['text'])
def func(message):
    global last_command_code
    if message.text == "Написать админам":
        last_command_code = 1
        bot.send_message(message.chat.id, text="Введите ваше сообщение:")
    elif message.text == "Оценка повреждений по фото":
        last_command_code = 2
        bot.send_message(message.chat.id, text="Отправьте фото повреждений: ")

    elif message.text == "Template-1":
        last_command_code = 3
        bot.send_message(message.chat.id, "Answer-1")

    elif message.text == "Template-1":
        last_command_code = 4
        bot.send_message(message.chat.id, text="Answer-2")

    elif message.text == "Вернуться в главное меню":
        last_command_code = 5
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Написать админам")
        button2 = types.KeyboardButton("Оценка повреждений по фото")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif last_command_code == 1:
        last_command_code = 0
        print("ЗАПИСЬ В БД")
        print(message.from_user)
        bot.send_message(message.chat.id, text="Сообщение будет передано админам. Хотите сделать что-то ещё?")
        is_answered = False
        string_to_db = (message.from_user.username, message.from_user.id, message.text, is_answered, datetime.date.today().isoformat())
        print(f"{string_to_db=}")

    else:
        last_command_code = 0
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован...")

