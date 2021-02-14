import logging
from telegram.ext import Updater, CommandHandler


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет пользователь! Ты вызвал команду СТРАТ')
    print(update)

def main():
    PASS = "1645080260:AAFPS09Z4lN8ShaI-W3p9Jk0H1i_QOdZGJQ"
    mybot = Updater(PASS, use_context=True, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    mybot.start_polling()
    mybot.idle()
    
main()