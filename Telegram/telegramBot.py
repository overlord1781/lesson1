import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logtime = '%(asctime)s %(message)s'
logdate = '%m/%d/%Y %I:%M:%S %p'
logging.basicConfig(filename='bot.log', level=20, format=logtime, datefmt=logdate) #Логирование событий бота


PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSOWRD }}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет пользователь! Ты вызвал команду СТРАТ')
    print(update)

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)
    
def main():
    PASS = settings.API_KEY
    mybot = Updater(PASS, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("бот запустился")

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()