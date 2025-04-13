import time

from utils import *
from telegram_modules.telegram_bot import bot

config = load_config("config.toml")
print(config)

# Запуск бота
bot.polling(none_stop=True)
