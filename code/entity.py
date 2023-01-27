class Message():

    content = ""
    wordle_share_detected = False
    wordle_result = None


class WordleResult():

    wordle_id = None
    desired_word = ""
    off_by_one = False
    lines = []