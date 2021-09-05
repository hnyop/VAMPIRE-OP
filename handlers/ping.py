from datetime import datetime
from time import time

from pyrogram import client as USER
from pyrogram.types import Message

@app.on_message(filters.text & cmd_filter('ping'))
async def ping(_, message):
    start = datetime.now()
    msg = await send('`Pong!`')
    end = datetime.now()
    latency = (end - start).microseconds / 1000
    await msg.edit(f"**Pong!**\n`{latency} ms`")