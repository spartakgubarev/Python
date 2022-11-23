from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *



app = ApplicationBuilder().token("5653417093:AAEOT_kwPw0vHD1Mr-erFPXb4eNhuX8E_8o").build()

app.add_handler(CommandHandler("hi", hi_command))

app.add_handler(CommandHandler("time", time_command))

app.add_handler(CommandHandler("help", help_command))

app.add_handler(CommandHandler("sum", sum_command))

app.add_handler(CommandHandler("sum", log))

app.add_handler(CommandHandler("url", url))


print('server start')

app.run_polling()
