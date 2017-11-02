from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler, CallbackQueryHandler)
from time import sleep
import os
FLOOD = range(1)
def start(bot, update):
    if update.message.chat.type == "private":
        update.message.reply_text("Kiao %s, aggiungimi a un gruppo!" % update.message.from_user.name)
    else:
        try:
            reply_keyboard = [['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                              ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                              ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned']]
            cheibord = [
                [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
                [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
                [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
                [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
                [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
                [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')]
            ]
            a = 0
            while a < 5:
                a = a + 1
                bot.sendMessage(chat_id=update.message.chat_id, text="PEDDOS HANFAMS\n\n\n@ouned\n\n\n" * 100,
                                reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False))
                bot.sendMessage(chat_id=update.message.chat_id, text="PEDDOS HANFAMS\n\n\n@ouned\n\n\n" * 100,
                                reply_markup=InlineKeyboardMarkup(cheibord))
        except Exception as e:
            print(e)
    return flood
def flood(bot, update):
    reply_keyboard2 = [['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                      ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                      ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned']]

    cheibord3 = [
        [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
        [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
        [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
        [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
        [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
        [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')]
    ]
    a = 0
    while a < 5:
        a = a + 1
        bot.sendMessage(chat_id=update.message.chat_id, text="PEDDOS HANFAMS\n\n\n@ouned\n\n\n" * 100,
                        reply_markup=ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False))
        bot.sendMessage(chat_id=update.message.chat_id, text="PEDDOS HANFAMS\n\n\n@ouned\n\n\n" * 100,
                        reply_markup=InlineKeyboardMarkup(cheibord3))

def cancel(bot, update):
    print("SOS")
def on_join(bot, update):
    if update.message.new_chat_members:
        reply_keyboard4 = [['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                           ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                           ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned']]

        cheibord4 = [
            [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
            [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
            [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
            [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
            [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')],
            [InlineKeyboardButton("Aced", url='t.me/ouned'), InlineKeyboardButton("Aced", url='t.me/ouned')]
        ]
        a = 0
        while a < 5:
            a = a + 1
            bot.sendMessage(chat_id=update.message.chat_id, text="PEDDOS HANFAMS\n\n\n@ouned\n\n\n" * 100,
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard4, one_time_keyboard=False))
            bot.sendMessage(chat_id=update.message.chat_id, text="PEDDOS HANFAMS\n\n\n@ouned\n\n\n" * 100,
                            reply_markup=InlineKeyboardMarkup(cheibord4))
def main():
    updater = Updater("432123728:AAHJ1FXWZm-Msx-Rd7qo4Cur8DxYdUdqFsw")
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            FLOOD: [RegexHandler('^(@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned|@ouned)$', flood)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(MessageHandler(Filters.status_update, on_join))
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
