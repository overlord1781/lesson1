import logging
from telegram.ext import Updater, CommandHandler


logtime = '%(asctime)s %(message)s'
logdate = '%m/%d/%Y %I:%M:%S %p'
logging.basicConfig(filename='bot.log', level=20, format=logtime, datefmt=logdate) #Логирование событий бота


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет пользователь! Ты вызвал команду СТРАТ')
    print(update)
    print(1/0)

def main():
    PASS = "1645080260:AAFPS09Z4lN8ShaI-W3p9Jk0H1i_QOdZGJQ"
    mybot = Updater(PASS, use_context=True, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    logging.info("бот запустился")

    mybot.start_polling()
    mybot.idle()
    
main()