import asyncio
import json
import discord


class DiscordBot(discord.Client):
    def __init__(self, parent=None):
        self.parent = parent

        # Init the superclass
        super().__init__()

        # Now get the key and run the bot
        with open('discord_credentials.json', 'r') as f:
            key = json.load(f)['discord_key']

        super().run(key)

        # Callback continues in on_ready()

    async def on_ready(self):
        self.parent.bot = self

    async def send(self, guild_id, channel_id, message):
        guild = self.get_guild(guild_id)
        channel = guild.get_channel(channel_id)
        await channel.send(message)

    async def dm(self, user_id, message):
        user = await self.fetch_user(user_id)
        await user.send(message)


def start_discord(parent, loop):
    asyncio.set_event_loop(loop)
    loop.run_forever(DiscordBot(parent))