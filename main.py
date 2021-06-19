from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from discordbot import start_discord, DiscordBot
import asyncio
import threading
import time


class Disc:
    def __init__(self):
        self.bot = None
        self.discord_loop = asyncio.new_event_loop()
        threading.Thread(target=start_discord, args=(self, self.discord_loop), daemon=True).start()
        while self.bot is None:
            time.sleep(0.5)
        print('Discord initialized.')

    async def send(self, guild, channel, text):
        asyncio.run_coroutine_threadsafe(self.bot.send(guild, channel, text), self.discord_loop)

    async def dm(self, recipient, text):
        asyncio.run_coroutine_threadsafe(self.bot.dm(recipient, text), self.discord_loop)


app = FastAPI()
disc = Disc()


class ChannelMessage(BaseModel):
    server: int
    channel: int
    text: str


class DirectMessage(BaseModel):
    recipient: int
    text: str


@app.post("/chat")
async def send_chat(message: ChannelMessage):
    await disc.send(message.server, message.channel, message.text)
    body = {
        "code": 0
    }
    return body


@app.post("/dm")
async def send_chat(message: DirectMessage):
    await disc.dm(message.recipient, message.text)
    body = {
        "code": 0
    }
    return body
