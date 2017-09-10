from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import logging
from time import sleep
import os
logging.basicConfig(format='[%(asctime)s] Errore tarocco:  %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
GENDER, PHOTO, LOCATION, BIO = range(4)
def start(bot, update):
    if update.message.chat.type == "private":
        update.message.reply_text("Zao!\nAggiungimi ad un gruppo e inizierò a stormare c:")
    else:
        reply_keyboard = [['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                          ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                          ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned']]
        a = 0
        print("aced")
        while a < 5:
            a = a + 1
            bot.sendMessage(chat_id=update.message.chat_id, text="@ouned\n"*100,
                             reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False))
        return GENDER
def gender(bot, update):
    reply_keyboard2 = [['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                      ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                      ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned']]
    a = 0
    while a < 5:
        a = a + 1
        bot.sendMessage(chat_id=update.message.chat_id, text="@ouned\n" * 100,
                        reply_markup=ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False))
def cancel(bot, update):
    print("SOS")
def on_join(bot, update):
    if update.message.new_chat_members:
        reply_keyboard3 = [['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                           ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                           ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned']]
        a = 0
        while a < 5:
            a = a + 1
            bot.sendMessage(chat_id=update.message.chat_id, text="@ouned\n" * 100,
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=False))
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
def main():
    updater = Updater("432123728:AAE5WqrSLuaY4gdez8sGmSndhLie1jvGaTw")
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            GENDER: [RegexHandler('^(@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned)$', gender)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(MessageHandler(Filters.status_update, on_join))
    dp.add_handler(conv_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
