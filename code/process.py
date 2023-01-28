import pickle
import sys
from entity import Message, WordleResult, WordleStats


# miss colors (theme dependent)
black_square = chr(11035)
white_square = chr(11036)

# normal colors (present, position)
yellow_square = chr(129000)
green_square = chr(129001)

# high contrast colors (present, position)
blue_square = chr(128998)
orange_square = chr(128999)

# array of the above
wordle_characters = [
    black_square,
    white_square,
    yellow_square,
    green_square,
    blue_square,
    orange_square
]


with open('dump.pkl', 'rb') as f, open('wordles.txt', 'rb') as g:

    message_collections = pickle.load(f)

    WordleStats().print_header()

    for author, message_collection_obj in message_collections.items():

        # Streak variables
        current_streak = 0
        max_streak = 0
        last_wordle_id = None

        stats = message_collection_obj.stats
        message_count = len(message_collection_obj.messages)
        # print(f'{author} message count: {message_count}')

        for message_index in range(0, message_count):

            message_obj = message_collection_obj.messages[message_index]

            # Check if message contains any of the used wordle characters
            found = False
            for wordle_character in wordle_characters:
                if wordle_character in message_obj.content:
                    found = True
                    break

            # Skip processing if message does not contain a wordle character
            if not found:
                continue

            # Skip processing if message does not start with Wordle
            if not message_obj.content.startswith('Wordle'):
                continue

            # This message is definitely a wordle share result
            message_obj.wordle_share_detected = True
            wordle_result_obj = WordleResult()

            # Increase n by one
            stats.n += 1

            # Extract ID
            bits = message_obj.content.split(' ')
            wordle_id = int(bits[1])
            wordle_result_obj.wordle_id = wordle_id

            # Get desired word from ID from wordle answer file
            g.seek(5 * wordle_id, 0)
            wordle_result_obj.desired_word = g.read(5)

            # Extract number of guesses and hard mode character
            result = bits[2].split('\n')[0]
            guesses = result[0]
            wordle_result_obj.guesses = guesses
            wordle_result_obj.hard_mode = True if result[-1] == '*' else False

            # Extracting emoji output:
            guess_lines = []
            bits = message_obj.content.split('\n')

            # Determine number of lines to process
            line_count = len(bits)
            if guesses == '6' or guesses == 'X':
                line_count = 8
            else:
                line_count = int(guesses) + 2

            # Skip the first two newline characters
            for index in range(2, line_count):

                guess_line = bits[index]

                # Store the guess characters
                wordle_result_obj.guess_lines.append(guess_line)

                # Quantify the value of the guess and store into stats
                value = 0
                value += guess_line.count(yellow_square) * 0.5
                value += guess_line.count(blue_square) * 0.5
                value += guess_line.count(green_square)
                value += guess_line.count(orange_square)
                wordle_result_obj.guess_values.append(value)

                # Check off_by_one criteria
                if guesses != 'X' and value >= 3.5 and int(guesses) == index:
                    wordle_result_obj.off_by_one = True
                    stats.off_by_one_count += 1

                # Update wordle stats with above information
                if index == 2:
                    stats.total_1_value += value
                    stats.total_1_guesses += 1
                elif index == 3:
                    stats.total_2_value += value
                    stats.total_2_guesses += 1
                elif index == 4:
                    stats.total_3_value += value
                    stats.total_3_guesses += 1
                elif index == 5:
                    stats.total_4_value += value
                    stats.total_4_guesses += 1
                elif index == 6:
                    stats.total_5_value += value
                    stats.total_5_guesses += 1
                elif index == 7:
                    stats.total_6_value += value
                    stats.total_6_guesses += 1

            # Update guess totals
            if guesses == '1':
                stats.total_1_results += 1
            elif guesses == '2':
                stats.total_2_results += 1
            elif guesses == '3':
                stats.total_3_results += 1
            elif guesses == '4':
                stats.total_4_results += 1
            elif guesses == '5':
                stats.total_5_results += 1
            elif guesses == '6':
                stats.total_6_results += 1
            elif guesses == 'X':
                stats.total_X_results += 1
            else:
                sys.exit("Unsupported result entered: (?/6)")

            # Increment if starting streak or current wordle_id is consecutive
            #   >= to handle cases where duplicate wordle posting
            if current_streak == 0 or last_wordle_id >= wordle_id - 1:
                current_streak += 1
            else:
                # Update max_streak if current_streak is larger
                if current_streak > max_streak:
                    max_streak = current_streak

                # reset streak
                current_streak = 0

            last_wordle_id = wordle_id

            # Add populated wordle_result to message class
            message_obj.wordle_result = wordle_result_obj
        
        # Update max_streak if current_streak is larger
        if current_streak > max_streak:
            max_streak = current_streak

        stats.current_streak = current_streak
        stats.max_streak = max_streak

        # Calculate average stats
        if stats.n != 0:

            stats.score += stats.total_1_results
            stats.score += stats.total_2_results * 2
            stats.score += stats.total_3_results * 3
            stats.score += stats.total_4_results * 4
            stats.score += stats.total_5_results * 5
            stats.score += stats.total_6_results * 6
            stats.score += stats.total_X_results * 7
            stats.score = round(stats.score / stats.n, 2) 

            stats.avg_off_by_one_count = round(100 * (stats.off_by_one_count / stats.n), 2)

            stats.avg_1_results = round(100 * (stats.total_1_results / stats.n), 2)
            stats.avg_2_results = round(100 * (stats.total_2_results / stats.n), 2)
            stats.avg_3_results = round(100 * (stats.total_3_results / stats.n), 2)
            stats.avg_4_results = round(100 * (stats.total_4_results / stats.n), 2)
            stats.avg_5_results = round(100 * (stats.total_5_results / stats.n), 2)
            stats.avg_6_results = round(100 * (stats.total_6_results / stats.n), 2)
            stats.avg_X_results = round(100 * (stats.total_X_results / stats.n), 2)

            if stats.total_1_guesses:
                stats.avg_1_value = round(stats.total_1_value / stats.total_1_guesses, 2)
            if stats.total_2_guesses:
                stats.avg_2_value = round(stats.total_2_value / stats.total_2_guesses, 2)
            if stats.total_3_guesses:
                stats.avg_3_value = round(stats.total_3_value / stats.total_3_guesses, 2)
            if stats.total_4_guesses:
                stats.avg_4_value = round(stats.total_4_value / stats.total_4_guesses, 2)
            if stats.total_5_guesses:
                stats.avg_5_value = round(stats.total_5_value / stats.total_5_guesses, 2)
            if stats.total_6_guesses:
                stats.avg_6_value = round(stats.total_6_value / stats.total_6_guesses, 2)

            stats.print(author)