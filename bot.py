import ephem
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Call /start')
    update.message.reply_text('Hello')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def handle_planet(update, context):
    text = update.message.text
    getPlanet = text.split(' ')
    nameofplanet = getPlanet[1]

    if nameofplanet == 'mars':
        mars = ephem.Mars('2000/01/01')
        constellation = ephem.constellation(mars)
        update.message.reply_text(constellation)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", handle_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
