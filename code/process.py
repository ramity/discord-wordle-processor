import pickle

new_line = 10

# miss colors (theme dependent)
black_square = 11035
white_square = 11036

# normal colors
yellow_square = 129000
green_square = 129001

# high contrast colors
blue_square = 128998
orange_square = 128999

wordle_characters = [
    black_square,
    white_square,
    yellow_square,
    green_square,
    blue_square,
    orange_square
]

results_obj = {}

with open('dump.pkl', 'rb') as f:
    messages_obj = pickle.load(f)

    for author, messages in messages_obj.items():

        # print(f'{author} message count: {len(messages)}')

        results_obj[author] = []

        for message in messages:

            # Check if message contains any of the used wordle characters
            found = False
            for wordle_character in wordle_characters:
                if chr(wordle_character) in message:
                    found = True
                    break
            
            # Skip processing if message does not contain wordle character
            if not found:
                continue

            # Detecting if message starts with Wordle and extract #/# result
            if message.startswith('Wordle'):
                bits = message.split(' ')
                result = bits[2].split('\n')[0]
                results_obj[author].append(result)

            # for character in message:
            #     # print(repr(character), ord(character))
            #     pass

# Remove authors with empty results
for author, results in list(results_obj.items()):
    if results == []:
        del results_obj[author]

results_bins = {}

# Calculating bins
for author, results in results_obj.items():
    results_bins[author] = {}
    results_bins[author]['1'] = 0
    results_bins[author]['2'] = 0
    results_bins[author]['3'] = 0
    results_bins[author]['4'] = 0
    results_bins[author]['5'] = 0
    results_bins[author]['6'] = 0
    results_bins[author]['X'] = 0
    results_bins[author]['count'] = 0

    # Increment applicable bin and count
    for result in results:
        results_bins[author][result[0]] += 1
        results_bins[author]['count'] += 1

    # Calculate weighted score
    score = 0
    score += results_bins[author]['1']
    score += results_bins[author]['2'] * 2
    score += results_bins[author]['3'] * 3
    score += results_bins[author]['4'] * 4
    score += results_bins[author]['5'] * 5
    score += results_bins[author]['6'] * 6
    score += results_bins[author]['X'] * 7
    results_bins[author]['score'] = round((score / results_bins[author]['count']) * 100, 1)

# Use bin frequency / total count to calculate bin rate
for author, results in results_obj.items():

    # Calculate bin rate
    results_bins[author]['1%'] = round((results_bins[author]['1'] / results_bins[author]['count']) * 100, 1)
    results_bins[author]['2%'] = round((results_bins[author]['2'] / results_bins[author]['count']) * 100, 1)
    results_bins[author]['3%'] = round((results_bins[author]['3'] / results_bins[author]['count']) * 100, 1)
    results_bins[author]['4%'] = round((results_bins[author]['4'] / results_bins[author]['count']) * 100, 1)
    results_bins[author]['5%'] = round((results_bins[author]['5'] / results_bins[author]['count']) * 100, 1)
    results_bins[author]['6%'] = round((results_bins[author]['6'] / results_bins[author]['count']) * 100, 1)
    results_bins[author]['X%'] = round((results_bins[author]['X'] / results_bins[author]['count']) * 100, 1)

# Fancy print the results
print('Name\r\t\t1%\t2%\t3%\t4%\t5%\t6%\tX%\tscore')
print('-'*77)
for author, results in results_bins.items():
    output = ''
    output += author + '\r\t\t'
    output += str(results['1%']) + '\t'
    output += str(results['2%']) + '\t'
    output += str(results['3%']) + '\t'
    output += str(results['4%']) + '\t'
    output += str(results['5%']) + '\t'
    output += str(results['6%']) + '\t'
    output += str(results['X%']) + '\t'
    output += str(results['score'])
    print(output)