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

with open('dump.pkl', 'rb') as f:
    messages = pickle.load(f)

    print(f'Message count: {len(messages)}')

    for message in messages:
        for string in message:
            for character in string:

                print(repr(character), ord(character))
        
        print('-'*42)
        break