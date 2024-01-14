import os
import discord
import logging
import pickle
import asyncio
from entity import MessageCollection, Message, WordleStats

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

class MyClient(discord.Client):

    # Attach to on_ready event
    async def on_ready(self):

        # Print some verbose messages to console
        print('Logged on as ' + str(self.user))
        print('Pulling messages from the #' + str(os.getenv('CHANNEL')) + ' text channel')

        output = {}
        channel = self.get_wordle_channel()

        # # Iterate over channel history
        async for message in channel.history(limit = int(os.getenv('LIMIT')), oldest_first = True):

            author = message.author.name

            # Make sure author key is present before appending
            if author not in output:
                message_collection_obj = MessageCollection()
                message_collection_obj.stats = WordleStats()
                output[author] = message_collection_obj

            message_obj = Message()
            message_obj.content = message.content
            output[author].messages.append(message_obj)

        print('Loaded all messages')

        with open('dump.pkl', 'wb') as f:
            pickle.dump(output, f)

        print('Saved all messages')
        print('Exiting')

    # Get context of text channel defined by CHANNEL env var
    def get_wordle_channel(self):
        for server in self.guilds:
            for channel in server.channels:
                if str(channel.type) == 'text' and str(channel.name) == str(os.getenv('CHANNEL')):
                    return channel

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents = intents)
client.run(os.getenv('TOKEN'), log_handler = handler)
