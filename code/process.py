import pickle

with open('dump.pkl', 'rb') as f:
    messages = pickle.load(f)

    print(f'Message count: {len(messages)}')

    for string in messages[59]:

        for character in string:

            print(repr(character), ord(character))