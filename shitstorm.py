from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler, CallbackQueryHandler)
from time import sleep
import os
FLOOD = range(1)


reply_keyboard = [['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                      ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned'],
                      ['@ouned', '@ouned', '@ouned', '@ouned', '@ouned']]
inline_keyboard = [
        [InlineKeyboardButton("👺", url='t.me/ouned'), InlineKeyboardButton("👺", url='t.me/ouned')],
        [InlineKeyboardButton("👺", url='t.me/ouned'), InlineKeyboardButton("👺", url='t.me/ouned')],
        [InlineKeyboardButton("👺", url='t.me/ouned'), InlineKeyboardButton("👺", url='t.me/ouned')],
        [InlineKeyboardButton("👺", url='t.me/ouned'), InlineKeyboardButton("👺", url='t.me/ouned')],
        [InlineKeyboardButton("👺", url='t.me/ouned'), InlineKeyboardButton("👺", url='t.me/ouned')],
        [InlineKeyboardButton("👺", url='t.me/ouned'), InlineKeyboardButton("👺", url='t.me/ouned')]
    ]

def start(bot, update):
    global reply_keyboard, inline_keyboard
    if update.message.chat.type == "private":
        update.message.reply_text("Kiao %s, aggiungimi a un gruppo!" % update.message.from_user.name)
    else:
        a = 0
        while a < 5:
            a = a + 1
            bot.sendMessage(chat_id=update.message.chat_id, text="@Ouned 👺\n\n\n👺👺👺👺👺\n\n\n" * 100,
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False))
            bot.sendMessage(chat_id=update.message.chat_id, text="@ouned 👺\n\n\n👺👺👺👺👺\n\n\n" * 100,
                            reply_markup=InlineKeyboardMarkup(inline_keyboard))
    return flood
def flood(bot, update):
    global reply_keyboard, inline_keyboard
    a = 0
    while a < 5:
        a = a + 1
        bot.sendMessage(chat_id=update.message.chat_id, text="@Ouned 👺\n\n\n👺👺👺👺👺\n\n\n" * 100,
                        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False))
        bot.sendMessage(chat_id=update.message.chat_id, text="@ouned 👺\n\n\n👺👺👺👺👺\n\n\n" * 100,
                        reply_markup=InlineKeyboardMarkup(inline_keyboard))

def cancel():
    print("SOS")
def on_join(bot, update):
    global reply_keyboard, inline_keyboard
    if update.message.new_chat_members:
        a = 0
        while a < 5:
            a = a + 1
            bot.sendMessage(chat_id=update.message.chat_id, text="@Ouned 👺\n\n\n👺👺👺👺👺\n\n\n" * 100,
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False))
            bot.sendMessage(chat_id=update.message.chat_id, text="@ouned 👺\n\n\n👺👺👺👺👺\n\n\n" * 100,
                            reply_markup=InlineKeyboardMarkup(inline_keyboard))
def main():
    updater = Updater("432123728:AAElJkRP6anMgQcq9x3eGps0-cj1FZ-EFrc")
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