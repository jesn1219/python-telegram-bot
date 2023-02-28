import sys
import telegram
import asyncio


class jesnk_Wrapper :
    def __init__(self,token,chatId) :
        self.token = token
        #self.telBot = telegram.Bot(token=TEL_TOKEN)
        self.telChatId = chatId

    def sendMessage(self,text) :
        self.telBot = telegram.Bot(self.token)
        asyncio.run(self.telBot.sendMessage(chat_id=self.telChatId, text=text))

    def sendFile(self, filePath) :
        self.telBot = telegram.Bot(self.token)
        f = open(filePath, 'rb')
        asyncio.run(self.telBot.sendDocument(chat_id=self.telChatId, document=f))

    def sendImage(self, imagePath) :
        self.telBot = telegram.Bot(self.token)
        f = open(imagePath, 'rb')
        asyncio.run(self.telBot.sendPhoto(chat_id=self.telChatId, photo=f))



