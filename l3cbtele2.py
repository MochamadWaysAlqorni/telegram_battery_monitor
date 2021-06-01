import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import subprocess
import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Ini adalah bot untuk mengetahui info baterai. Masukkan /help untuk bantuan')

def help(update, context):
    update.message.reply_text('Masukkan pesan /batt untuk mengetahui info baterai.\nMasukkan /info untuk mengetahui informasi app bot.')
    
def battinfo(update, context):
    with open('battery_log.txt') as f:
        for line in (f.readlines() [-4:]):
            update.message.reply_text(line)
    print("data sent : OK")   
    
def infoapp(update, context):
    update.message.reply_text('Battery Information App by...\n\nKelompok 2 (3 D3 TA) : \n1. Mochamad Ways Alqorni. \n2. Tia Cahyani. \n3. Ulfa Aida Uswatul Khasanah')


def echo(update, context):
    update.message.reply_text(update.message.text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main3():
    """Start the bot."""
    updater = Updater("1752527330:AAFZ_UEsZI2hAPRKBtq5hXLC527R_cUCSfo", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("batt", battinfo))
    dp.add_handler(CommandHandler("info", infoapp))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main3()