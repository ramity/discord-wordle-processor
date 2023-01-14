import os
import discord
import logging
import pickle

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        print(f'Pulling messages from #wordle textchannel.')

        messages = {}
        channel = self.get_wordle_channel()

        async for message in channel.history(limit=4000, oldest_first=True):
            author = message.author.name
            if author not in messages:
                messages[author] = []
            messages[author].append(message.content)

        print(f'Loaded all messages.')

        with open('dump.pkl', 'wb') as f:
            pickle.dump(messages, f)

        print(f'Saved all messages.')
        print(f'Exiting.')

        await self.close()

    def get_wordle_channel(self):
        for server in self.guilds:
            for channel in server.channels:
                if str(channel.type) == 'text' and str(channel.name) == os.getenv('CHANNEL')':
                    return channel

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'), log_handler=handler)
