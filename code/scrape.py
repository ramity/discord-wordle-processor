import os
import discord
import logging
import pickle
import json
import asyncio
import sys

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

class WordleScrapingClient(discord.Client):

    # Data
    wordles_by_author = {}
    wordle_stats_by_author = {}
    wordle_answer_file = None

    # Static wordle values
    black_square = chr(11035)
    white_square = chr(11036)

    # Normal colors (present, position)
    yellow_square = chr(129000)
    green_square = chr(129001)

    # High contrast colors (present, position)
    blue_square = chr(128998)
    orange_square = chr(128999)

    # Wordle character array
    wordle_characters = [
        black_square,
        white_square,
        yellow_square,
        green_square,
        blue_square,
        orange_square
    ]

    # Attach to on_ready event
    async def on_ready(self):

        # Print some verbose messages to console
        print('Logged on as ' + str(self.user))

        # Open wordles.txt file context
        self.wordle_answer_file = open('wordles.txt', 'rb')

        # Initiate scraping wordle channel
        print('Pulling messages from the #' + str(os.getenv('CHANNEL')) + ' text channel')
        await self.scrape_wordle_channel()

        # Calculate streak stats
        print('Calculating stats')
        self.calculate_average_stats()
        self.calculate_streak_stats()

        # Save data
        self.save_to_disk()

        # Close wordles.txt file context
        self.wordle_answer_file.close()

    # Scrapes the wordle channel and inline calculates statistics
    async def scrape_wordle_channel(self):

        channel = self.get_wordle_channel()

        # Iterate over channel history
        async for message in channel.history(limit = int(os.getenv('LIMIT')), oldest_first = True):

            author = message.author.name
            message_content = message.content

            # Skip if message is not a wordle share
            if not self.message_is_wordle_share(message_content):
                continue

            # Handle wordle message
            self.process_wordle_message(author, message_content)

    # Get context of text channel defined by CHANNEL env var
    def get_wordle_channel(self):
        for server in self.guilds:
            for channel in server.channels:
                if str(channel.type) == 'text' and str(channel.name) == str(os.getenv('CHANNEL')):
                    return channel

    # Returns if the message is a worlde share or not
    def message_is_wordle_share(self, message):

        # Skip processing if message does not start with Wordle
        if not message.startswith('Wordle'):
            return False

        # Check if message contains any of the used wordle characters
        found = False
        for wordle_character in self.wordle_characters:
            if wordle_character in message:
                return True

        # Did not find a wordle character
        return False

    # Processes incoming wordle message, updates stats, and adds record
    def process_wordle_message(self, author, message_content):

        # Init needed vars
        self.init_wordle_stats_for_author(author)

        wordle = {}

        # Update author's n by 1
        self.wordle_stats_by_author[author]['n'] += 1

        # Extract ID
        # - remove comma prior to int cast
        bits = message_content.split(' ')
        ID = int(bits[1].replace(',', ''))
        wordle['ID'] = ID

        # Extract desired word
        self.wordle_answer_file.seek(5 * ID, 0)
        word = self.wordle_answer_file.read(5)
        wordle['word'] = word.decode('utf-8')

        # Extract the resultant number of guesses and hardmode character
        # - Handle party emoji added on wordle 1000
        if len(bits[2]) > 1:
            guesses = bits[2][0]
            hard_mode = True if bits[2][2] == '*' else False
        else:
            guesses = bits[3][0]
            hard_mode = True if bits[3][2] == '*' else False
        guesses_value = int(guesses) if guesses != 'X' else 6
        wordle['hardMode'] = hard_mode
        wordle['result'] = guesses
        wordle['resultValue'] = guesses_value
        wordle['offByOne'] = False

        # Extract guess lines
        line_break_count = message_content.count('\n')
        # - Regular case
        if line_break_count >= guesses_value:
            guess_lines = message_content.split('\n')[2:2 + guesses_value]
        # - \n's converted to single space case
        elif line_break_count == 0:
            guess_lines = bits[3:3 + guesses_value]
        else:
            print("Malformed result detected by {}@ID:{}".format(author, wordle_id))
            return False
        wordle['guesses'] = guess_lines

        # Process guess lines
        for index, guess in enumerate(guess_lines):

            # Quantify the value of the guess
            value = self.calculate_wordle_guess_value(guess)

            # Check if this wordle guess meets the offByOne criteria
            if value >= 3.5 and value < 5 and guesses_value - 2 == index:
                wordle['offByOne'] = True
                self.wordle_stats_by_author[author]['offByOneCount'] += 1

            # Update authors wordle stats with guess value
            if index == 0:
                self.wordle_stats_by_author[author]['guess1ValueSum'] += value 
                self.wordle_stats_by_author[author]['guess1Count'] += 1
            elif index == 1:
                self.wordle_stats_by_author[author]['guess2ValueSum'] += value 
                self.wordle_stats_by_author[author]['guess2Count'] += 1
            elif index == 2:
                self.wordle_stats_by_author[author]['guess3ValueSum'] += value 
                self.wordle_stats_by_author[author]['guess3Count'] += 1
            elif index == 3:
                self.wordle_stats_by_author[author]['guess4ValueSum'] += value 
                self.wordle_stats_by_author[author]['guess4Count'] += 1
            elif index == 4:
                self.wordle_stats_by_author[author]['guess5ValueSum'] += value 
                self.wordle_stats_by_author[author]['guess5Count'] += 1
            elif index == 5:
                self.wordle_stats_by_author[author]['guess6ValueSum'] += value 
                self.wordle_stats_by_author[author]['guess6Count'] += 1

        # Update result counts
        if guesses == '1':
            self.wordle_stats_by_author[author]['result1Count'] += 1
        elif guesses == '2':
            self.wordle_stats_by_author[author]['result2Count'] += 1
        elif guesses == '3':
            self.wordle_stats_by_author[author]['result3Count'] += 1
        elif guesses == '4':
            self.wordle_stats_by_author[author]['result4Count'] += 1
        elif guesses == '5':
            self.wordle_stats_by_author[author]['result5Count'] += 1
        elif guesses == '6':
            self.wordle_stats_by_author[author]['result6Count'] += 1
        elif guesses == 'X':
            self.wordle_stats_by_author[author]['resultXCount'] += 1

        self.wordles_by_author[author].append(wordle)

    # Initializes the class attributes needed to store wordle results and stats
    def init_wordle_stats_for_author(self, author):

        # Conditionally create author key if it is not present
        if author not in self.wordle_stats_by_author:

            # Init containers
            self.wordle_stats_by_author[author] = {}
            self.wordles_by_author[author] = []

            # Stores number of wordles published by this author
            self.wordle_stats_by_author[author]['n'] = 0

            # Stores the average value of all past results
            self.wordle_stats_by_author[author]['score'] = 0

            # Stores the number of "OffByOne" instances
            self.wordle_stats_by_author[author]['offByOneCount'] = 0
            self.wordle_stats_by_author[author]['offByOneAverage'] = 0

            # Stores the value sums and counts for each guess index
            self.wordle_stats_by_author[author]['guess1ValueSum'] = 0
            self.wordle_stats_by_author[author]['guess1Count'] = 0
            self.wordle_stats_by_author[author]['guess1Average'] = 0
            self.wordle_stats_by_author[author]['guess2ValueSum'] = 0
            self.wordle_stats_by_author[author]['guess2Count'] = 0
            self.wordle_stats_by_author[author]['guess2Average'] = 0
            self.wordle_stats_by_author[author]['guess3ValueSum'] = 0
            self.wordle_stats_by_author[author]['guess3Count'] = 0
            self.wordle_stats_by_author[author]['guess3Average'] = 0
            self.wordle_stats_by_author[author]['guess4ValueSum'] = 0
            self.wordle_stats_by_author[author]['guess4Count'] = 0
            self.wordle_stats_by_author[author]['guess4Average'] = 0
            self.wordle_stats_by_author[author]['guess5ValueSum'] = 0
            self.wordle_stats_by_author[author]['guess5Count'] = 0
            self.wordle_stats_by_author[author]['guess5Average'] = 0
            self.wordle_stats_by_author[author]['guess6ValueSum'] = 0
            self.wordle_stats_by_author[author]['guess6Count'] = 0
            self.wordle_stats_by_author[author]['guess6Average'] = 0

            # Stores the wordle result counts
            self.wordle_stats_by_author[author]['result1Count'] = 0
            self.wordle_stats_by_author[author]['result1Average'] = 0
            self.wordle_stats_by_author[author]['result2Count'] = 0
            self.wordle_stats_by_author[author]['result2Average'] = 0
            self.wordle_stats_by_author[author]['result3Count'] = 0
            self.wordle_stats_by_author[author]['result3Average'] = 0
            self.wordle_stats_by_author[author]['result4Count'] = 0
            self.wordle_stats_by_author[author]['result4Average'] = 0
            self.wordle_stats_by_author[author]['result5Count'] = 0
            self.wordle_stats_by_author[author]['result5Average'] = 0
            self.wordle_stats_by_author[author]['result6Count'] = 0
            self.wordle_stats_by_author[author]['result6Average'] = 0
            self.wordle_stats_by_author[author]['resultXCount'] = 0
            self.wordle_stats_by_author[author]['resultXAverage'] = 0

            # Streak stats
            self.wordle_stats_by_author[author]['currentXLessStreak'] = 0
            self.wordle_stats_by_author[author]['currentPostStreak'] = 0
            self.wordle_stats_by_author[author]['currentCombinedStreak'] = 0
            self.wordle_stats_by_author[author]['maxXLessStreak'] = 0
            self.wordle_stats_by_author[author]['maxPostStreak'] = 0
            self.wordle_stats_by_author[author]['maxCombinedStreak'] = 0

    # Calculates the value of a wordle guess
    def calculate_wordle_guess_value(self, guess):

        value = 0
        value += guess.count(self.yellow_square) * 0.5
        value += guess.count(self.blue_square) * 0.5
        value += guess.count(self.green_square)
        value += guess.count(self.orange_square)
        return value

    # Calculates streak related stats for each author
    def calculate_streak_stats(self):

        for author, wordles in self.wordles_by_author.items():

            x_less_streak = 0
            post_streak = 0
            combined_streak = 0
            max_x_less_streak = 0
            max_post_streak = 0
            max_combined_streak = 0
            last_wordle_id = None

            for wordle in wordles:

                wordle_id = wordle['ID']
                guesses = wordle['result']

                # Combined streak check
                if (post_streak == 0 or last_wordle_id >= wordle_id - 1) and (x_less_streak == 0 or guesses != 'X'):
                    combined_streak += 1

                # Post streak check
                if post_streak == 0 or last_wordle_id >= wordle_id - 1:
                    post_streak += 1
                else:
                    # Update max_streaks
                    if post_streak > max_post_streak:
                        max_post_streak = post_streak
                    if combined_streak > max_combined_streak:
                        max_combined_streak = combined_streak

                    # reset streaks
                    post_streak = 0
                    combined_streak = 0

                # X-less streak check
                if x_less_streak == 0 or guesses != 'X':
                    x_less_streak += 1
                else:
                    # Update max streaks
                    if x_less_streak > max_x_less_streak:
                        max_x_less_streak = x_less_streak
                    if combined_streak > max_combined_streak:
                        max_combined_streak = combined_streak

                    # reset streaks
                    x_less_streak = 0
                    combined_streak = 0

                last_wordle_id = wordle_id
            
            # Update max streaks if current streaks are larger
            if post_streak > max_post_streak:
                max_post_streak = post_streak
            if x_less_streak > max_x_less_streak:
                max_x_less_streak = x_less_streak
            if combined_streak > max_combined_streak:
                max_combined_streak = combined_streak
            
            self.wordle_stats_by_author[author]['currentXLessStreak'] = x_less_streak
            self.wordle_stats_by_author[author]['currentPostStreak'] = post_streak
            self.wordle_stats_by_author[author]['currentCombinedStreak'] = combined_streak
            self.wordle_stats_by_author[author]['maxXLessStreak'] = max_x_less_streak
            self.wordle_stats_by_author[author]['maxPostStreak'] = max_post_streak
            self.wordle_stats_by_author[author]['maxCombinedStreak'] = max_combined_streak

    # Calculates average stats for each author
    def calculate_average_stats(self):

        for author in self.wordle_stats_by_author:

            score = 0
            score += self.wordle_stats_by_author[author]['result1Count']
            score += self.wordle_stats_by_author[author]['result2Count'] * 2
            score += self.wordle_stats_by_author[author]['result3Count'] * 3
            score += self.wordle_stats_by_author[author]['result4Count'] * 4
            score += self.wordle_stats_by_author[author]['result5Count'] * 5
            score += self.wordle_stats_by_author[author]['result6Count'] * 6
            score += self.wordle_stats_by_author[author]['resultXCount'] * 7
            self.wordle_stats_by_author[author]['score'] = round(score / self.wordle_stats_by_author[author]['n'], 2)

            self.wordle_stats_by_author[author]['offByOneAverage'] = round(100 * (self.wordle_stats_by_author[author]['offByOneCount'] / self.wordle_stats_by_author[author]['n']), 2)

            self.wordle_stats_by_author[author]['result1Average'] = round(100 * (self.wordle_stats_by_author[author]['result1Count'] / self.wordle_stats_by_author[author]['n']), 2)
            self.wordle_stats_by_author[author]['result2Average'] = round(100 * (self.wordle_stats_by_author[author]['result2Count'] / self.wordle_stats_by_author[author]['n']), 2)
            self.wordle_stats_by_author[author]['result3Average'] = round(100 * (self.wordle_stats_by_author[author]['result3Count'] / self.wordle_stats_by_author[author]['n']), 2)
            self.wordle_stats_by_author[author]['result4Average'] = round(100 * (self.wordle_stats_by_author[author]['result4Count'] / self.wordle_stats_by_author[author]['n']), 2)
            self.wordle_stats_by_author[author]['result5Average'] = round(100 * (self.wordle_stats_by_author[author]['result5Count'] / self.wordle_stats_by_author[author]['n']), 2)
            self.wordle_stats_by_author[author]['result6Average'] = round(100 * (self.wordle_stats_by_author[author]['result6Count'] / self.wordle_stats_by_author[author]['n']), 2)
            self.wordle_stats_by_author[author]['resultXAverage'] = round(100 * (self.wordle_stats_by_author[author]['resultXCount'] / self.wordle_stats_by_author[author]['n']), 2)

            self.wordle_stats_by_author[author]['guess1Average'] = round(self.wordle_stats_by_author[author]['guess1ValueSum'] / self.wordle_stats_by_author[author]['guess1Count'], 2)
            self.wordle_stats_by_author[author]['guess2Average'] = round(self.wordle_stats_by_author[author]['guess2ValueSum'] / self.wordle_stats_by_author[author]['guess2Count'], 2)
            self.wordle_stats_by_author[author]['guess3Average'] = round(self.wordle_stats_by_author[author]['guess3ValueSum'] / self.wordle_stats_by_author[author]['guess3Count'], 2)
            self.wordle_stats_by_author[author]['guess4Average'] = round(self.wordle_stats_by_author[author]['guess4ValueSum'] / self.wordle_stats_by_author[author]['guess4Count'], 2)
            self.wordle_stats_by_author[author]['guess5Average'] = round(self.wordle_stats_by_author[author]['guess5ValueSum'] / self.wordle_stats_by_author[author]['guess5Count'], 2)
            self.wordle_stats_by_author[author]['guess6Average'] = round(self.wordle_stats_by_author[author]['guess6ValueSum'] / self.wordle_stats_by_author[author]['guess6Count'], 2)

    # Saves calculated stats to disk
    def save_to_disk(self):

        with open('wordles-by-author.json', 'w') as f:
            json.dump(self.wordles_by_author, f, indent = 4)
        
        with open('wordle-stats-by-author.json', 'w') as f:
            json.dump(self.wordle_stats_by_author, f, indent = 4)

intents = discord.Intents.default()
intents.message_content = True

client = WordleScrapingClient(intents = intents)
client.run(os.getenv('TOKEN'), log_handler = handler)
