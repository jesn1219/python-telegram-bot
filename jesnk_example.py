# get user info from jesnk_info.json

from telegram.jesnk import jesnk_Wrapper
import json
import os
import sys
import time

user_info = json.load(open("jesnk_info.json"))
telegram_token = user_info["telegram"]['token']
telegram_chatid = user_info["telegram"]['chatid']

if __name__ == "__main__":
    # send message
    bot = jesnk_Wrapper(telegram_token, telegram_chatid)
    bot.sendMessage("Hello World!")
    bot.sendFile("test_files/test.txt")
    bot.sendImage("test_files/test.png")

