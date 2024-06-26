import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6426072097:AAFpvNEzW65qVT6XwTxzafDLJKFk-Xtbun0")

API_ID = int(os.environ.get("API_ID", "6119632"))

API_HASH = os.environ.get("API_HASH", "5b51582f938e93c8eab32612d5045737")

STRING = os.environ.get("STRING", "5b51582f938e93c8eab32612d5045737")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
