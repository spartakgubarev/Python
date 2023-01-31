from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
from fractions import Fraction


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update, context)
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/fraction (пример: fraction 12/45 25/32)\n/url\n/complex (пример 10 20)')


async def fraction_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()  # /sum 12/45 25/32
    items = ' '.join(items[1:])
    items = list(map(int, (items.replace('/', ' ')).split()))
    a = Fraction(items[0], items[1])
    b = Fraction(items[2], items[3])
    c = a+b
    await update.message.reply_text(f'{a} + {b} = {c}')


async def complex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()  # /complex 123 456
    a = int(items[1])
    b = int(items[2])
    c = complex(a, b)

    await update.message.reply_text(f'{a} {b} = {c}')
