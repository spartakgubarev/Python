# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token(
    "5653417093:AAEOT_kwPw0vHD1Mr-erFPXb4eNhuX8E_8o").build()

app.add_handler(CommandHandler("hi", hi_command))

app.add_handler(CommandHandler("time", time_command))

app.add_handler(CommandHandler("help", help_command))

app.add_handler(CommandHandler("fraction", fraction_command))

app.add_handler(CommandHandler("complex", complex_command))

print('server start')

app.run_polling()
