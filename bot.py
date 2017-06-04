from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#define the function
import logging
import ephem
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    updater = Updater("387827342:AAFqs_ayIPBi-pcmjXyFRVqKqFz4mqrLpOM")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))   
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()
#launch the function

def greet_user(bot, update):
    text='Вызван /start'
    print(text)
    update.message.reply_text(text)

#### user - planet, bot -  при помощи условного оператора if и ephem.constellation отвечать, 
# в каком созвездии сегодня находится планета.

def planets(bot, update):
    user_text = update.message.text 
    planets_list=[p for *_, p in ephem._libastro.builtin_planets()]
    if user_text = planets_list
        plan = ephem.user_text('2017/06/03')
        answ=ephem.constellation(plan)
#     update.message.reply_text(answ)

# def talk_to_me(bot, update):
#     user_text = update.message.text 
#     print(user_text)
#     update.message.reply_text(user_text)

main()
