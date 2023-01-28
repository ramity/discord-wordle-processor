class MessageCollection():

    def __init__(self):

        self.messages = []
        self.stats = None


class Message():

    def __init__(self):

        self.content = ""
        self.wordle_share_detected = False
        self.wordle_result = None


class WordleResult():

    def __init__(self):

        self.wordle_id = None
        self.guesses = 0
        self.hard_mode = False
        self.desired_word = ""
        self.off_by_one = False
        self.guess_lines = []
        self.guess_values = []


class WordleStats():

    def __init__(self):

        self.n = 0

        self.score = 0
        self.max_streak = 0
        self.on_streak = False

        self.off_by_one_count = 0
        self.avg_off_by_one_count = 0

        self.total_1_results = 0
        self.total_2_results = 0
        self.total_3_results = 0
        self.total_4_results = 0
        self.total_5_results = 0
        self.total_6_results = 0
        self.total_X_results = 0

        self.avg_1_results = 0
        self.avg_2_results = 0
        self.avg_3_results = 0
        self.avg_4_results = 0
        self.avg_5_results = 0
        self.avg_6_results = 0
        self.avg_X_results = 0

        self.total_1_guesses = 0
        self.total_2_guesses = 0
        self.total_3_guesses = 0
        self.total_4_guesses = 0
        self.total_5_guesses = 0
        self.total_6_guesses = 0

        self.total_1_value = 0
        self.total_2_value = 0
        self.total_3_value = 0
        self.total_4_value = 0
        self.total_5_value = 0
        self.total_6_value = 0

        self.avg_1_value = 0
        self.avg_2_value = 0
        self.avg_3_value = 0
        self.avg_4_value = 0
        self.avg_5_value = 0
        self.avg_6_value = 0
    
    def print_short_header(self):

        print('Name\r\t\tCount\tScore\tStreak\tMax\tOby1\tOby1%')

    def print_short(self, author):

        output = ''
        output += author + '\r\t\t'
        output += str(self.n) + '\t'
        output += str(self.score) + '\t'
        output += str(self.current_streak) + '\t'
        output += str(self.max_streak) + '\t'
        output += str(self.off_by_one_count) + '\t'
        output += str(self.avg_off_by_one_count)
        print(output)

    def print_avg_results_header(self):

        print('Name\r\t\tCount\t1%\t2%\t3%\t4%\t5%\t6%\tX%')

    def print_avg_results(self, author):

        output = ''
        output += author + '\r\t\t'
        output += str(self.n) + '\t'
        output += str(self.avg_1_results) + '\t'
        output += str(self.avg_2_results) + '\t'
        output += str(self.avg_3_results) + '\t'
        output += str(self.avg_4_results) + '\t'
        output += str(self.avg_5_results) + '\t'
        output += str(self.avg_6_results) + '\t'
        output += str(self.avg_X_results)
        print(output)

    def print_avg_values_header(self):

        print('Name\r\t\tCount\t1 val\t2 val\t3 val\t4 val\t5 val\t6 val')

    def print_avg_values(self, author):

        output = ''
        output += author + '\r\t\t'
        output += str(self.n) + '\t'
        output += str(self.avg_1_value) + '\t'
        output += str(self.avg_2_value) + '\t'
        output += str(self.avg_3_value) + '\t'
        output += str(self.avg_4_value) + '\t'
        output += str(self.avg_5_value) + '\t'
        output += str(self.avg_6_value)
        print(output)

    def print_full_header(self):

        print('Name\r\t\tCount\tScore\tStreak\tMax\tOby1\tOby1%\t1%\t2%\t3%\t4%\t5%\t6%\tX%\t1 val\t2 val\t3 val\t4 val\t5 val\t6 val')

    def print_full(self, author):

        output = ''
        output += author + '\r\t\t'
        output += str(self.n) + '\t'
        output += str(self.score) + '\t'
        output += str(self.current_streak) + '\t'
        output += str(self.max_streak) + '\t'
        output += str(self.off_by_one_count) + '\t'
        output += str(self.avg_off_by_one_count) + '\t'
        output += str(self.avg_1_results) + '\t'
        output += str(self.avg_2_results) + '\t'
        output += str(self.avg_3_results) + '\t'
        output += str(self.avg_4_results) + '\t'
        output += str(self.avg_5_results) + '\t'
        output += str(self.avg_6_results) + '\t'
        output += str(self.avg_X_results) + '\t'
        output += str(self.avg_1_value) + '\t'
        output += str(self.avg_2_value) + '\t'
        output += str(self.avg_3_value) + '\t'
        output += str(self.avg_4_value) + '\t'
        output += str(self.avg_5_value) + '\t'
        output += str(self.avg_6_value)
        print(output)
