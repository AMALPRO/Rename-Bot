import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6426072097:AAFpvNEzW65qVT6XwTxzafDLJKFk-Xtbun0")

API_ID = int(os.environ.get("API_ID", "6119632"))

API_HASH = os.environ.get("API_HASH", "5b51582f938e93c8eab32612d5045737")

STRING = os.environ.get("STRING", "1BVtsOJ0BuxU8Byssa_oQycEq_GuZzedIecoJeuolkotKQiDAETgZtqcn4a9b8caaeP-I2O2guVbw5YEPIuR7QJTAzz5NqJCF_MIG2L61ZMfJFKwDzTUGNdRcRsUECEvgrGKvDG7-PBOzd5IrfGyV2qRS5WFG-KQMz86BMjkSsjPkzg8IW4jbz_ltQuKUsZj2tMxxkbBlgik_DJcOHDGhWZSCj4Kiq4CTz1b0riNEjahBCxphxSmPOC5J6QcVjpj-SH5ArMcimxfvpLDjlM270ct1w66oU2O2zN1ITrnI3BJzlx8jA1c3NCiuV7jTg8KvOuatv6yT7-pynJXxaOQdRBRqEtg_Cx0=")


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
