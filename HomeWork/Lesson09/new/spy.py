from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    path = 'G:/Учеба/Разработчик/repo/Python/HomeWork/Lesson09/new/log1.csv'
    file = open(path, 'a', encoding='utf-8')
    file.write(f'{datetime.datetime.now().time()};{update.effective_user.first_name}; {update.effective_user.id}; {update.message.text}\n')
    file.close()
