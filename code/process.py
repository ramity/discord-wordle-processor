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

# Query user for output format

while(True):

    output_prompt = '\n'
    output_prompt += 'Select an output type (type the corresponding number key and press enter).\n'
    output_prompt += '[0] - Short\n'
    output_prompt += '[1] - Average results\n'
    output_prompt += '[2] - Average values\n'
    output_prompt += '[3] - Streaks\n'
    output_prompt += '[4] - Full\n'
    output_prompt += '\n'

    try:
        output_type = input(output_prompt)
    except KeyboardInterrupt:
        sys.stdout.write('\r')
        sys.exit(1)

    if output_type != '0' and output_type != '1' and output_type != '2' and output_type != '3':
        print(f'\nInvalid input: {output_type}')
        continue
    else:
        print()
    
    if output_type == '0':
        WordleStats().print_short_header()
    elif output_type == '1':
        WordleStats().print_avg_results_header()
    elif output_type == '2':
        WordleStats().print_avg_values_header()
    elif output_type == '3':
        WordleStats().print_streaks_header()
    elif output_type == '4':
        WordleStats().print_full_header()

    with open('dump.pkl', 'rb') as f, open('wordles.txt', 'rb') as g:

        message_collections = pickle.load(f)

        for author, message_collection_obj in message_collections.items():

            # Streak variables
            x_less_streak = 0
            post_streak = 0
            combined_streak = 0
            max_x_less_streak = 0
            max_post_streak = 0
            max_combined_streak = 0
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
                guesses = bits[2][0]
                guesses_value = int(guesses) if guesses != 'X' else 6
                wordle_result_obj.guesses = guesses
                wordle_result_obj.hard_mode = True if bits[2][2] == '*' else False

                # Extract guess lines from message
                line_break_count = message_obj.content.count('\n')
                # - Regular case
                if line_break_count >= guesses_value:
                    guess_lines = message_obj.content.split('\n')[2:2 + guesses_value]
                # - \n's converted to single space case
                elif line_break_count == 0:
                    guess_lines = bits[3:3 + guesses_value]
                else:
                    print("Malformed result detected by {}@ID:{}".format(author, wordle_id))
                    continue

                # Store and process emoji guess lines:
                wordle_result_obj.guess_lines = guess_lines
                guess_count = len(guess_lines)
                for index in range(0, guess_count):

                    # Quantify the value of the guess and store into stats
                    value = 0
                    value += guess_lines[index].count(yellow_square) * 0.5
                    value += guess_lines[index].count(blue_square) * 0.5
                    value += guess_lines[index].count(green_square)
                    value += guess_lines[index].count(orange_square)
                    wordle_result_obj.guess_values.append(value)

                    # Check off_by_one criteria
                    if value >= 3.5 and value < 5 and guesses_value - 2 == index:
                        wordle_result_obj.off_by_one = True
                        stats.off_by_one_count += 1

                    # Update wordle stats with above information
                    if index == 0:
                        stats.total_1_value += value
                        stats.total_1_guesses += 1
                    elif index == 1:
                        stats.total_2_value += value
                        stats.total_2_guesses += 1
                    elif index == 2:
                        stats.total_3_value += value
                        stats.total_3_guesses += 1
                    elif index == 3:
                        stats.total_4_value += value
                        stats.total_4_guesses += 1
                    elif index == 4:
                        stats.total_5_value += value
                        stats.total_5_guesses += 1
                    elif index == 5:
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
                    sys.exit("Unsupported result entered: {}".format(guesses))

                # Increment if starting streak or current wordle_id is consecutive
                #   >= to handle cases where duplicate wordle posting
                if (post_streak == 0 or last_wordle_id >= wordle_id - 1) and (x_less_streak == 0 or guesses != 'X'):
                    combined_streak += 1

                if post_streak == 0 or last_wordle_id >= wordle_id - 1:
                    post_streak += 1
                else:
                    # Update max_streaks if current_streaks are larger
                    if post_streak > max_post_streak:
                        max_post_streak = post_streak

                    if combined_streak > max_combined_streak:
                        max_combined_streak = combined_streak

                    # reset streaks
                    post_streak = 0
                    combined_streak = 0

                if x_less_streak == 0 or guesses != 'X':
                    x_less_streak += 1
                else:
                    if x_less_streak > max_x_less_streak:
                        max_x_less_streak = x_less_streak
                    
                    if combined_streak > max_combined_streak:
                        max_combined_streak = combined_streak
                    
                    # reset streaks
                    x_less_streak = 0
                    combined_streak = 0

                last_wordle_id = wordle_id

                # Add populated wordle_result to message class
                message_obj.wordle_result = wordle_result_obj
            
            # Update max streaks if current streaks are larger
            if post_streak > max_post_streak:
                max_post_streak = post_streak
            if x_less_streak > max_x_less_streak:
                max_x_less_streak = x_less_streak
            if combined_streak > max_combined_streak:
                max_combined_streak = combined_streak

            # Set stats vars to local values
            stats.post_streak = post_streak
            stats.x_less_streak = x_less_streak
            stats.combined_streak = combined_streak
            stats.max_post_streak = max_post_streak
            stats.max_x_less_streak = max_x_less_streak
            stats.max_combined_streak = max_combined_streak

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
                
                if output_type == '0':
                    stats.print_short(author)
                elif output_type == '1':
                    stats.print_avg_results(author)
                elif output_type == '2':
                    stats.print_avg_values(author)
                elif output_type == '3':
                    stats.print_streaks(author)
                elif output_type == '4':
                    stats.print_full(author)