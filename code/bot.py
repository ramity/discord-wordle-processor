import os
import discord
import logging
import pickle

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        channel = self.get_wordle_channel()
        messages = [message.content async for message in channel.history(limit=4000, oldest_first=True)]

        with open('dump.pkl', 'wb') as f:
            pickle.dump(messages, f)
        
        await self.close()

    def get_wordle_channel(self):
        for server in self.guilds:
            for channel in server.channels:
                if str(channel.type) == 'text' and str(channel.name) == 'wordle':
                    return channel

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'), log_handler=handler)