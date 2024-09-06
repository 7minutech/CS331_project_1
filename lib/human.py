class Human:
    """Class representing a human player in rock paper scissors"""
    # style: capitalized MOVE_SET to show it's a constant
    # feat: added quit to move set to allow user to quit out of program
    __MOVE_SET = ["rock","paper", "scissors", "quit"]
    def __init__(self):
        self.__move = ""
        self.__wins = 0
        self.__ties = 0
        self.__losses = 0
    def __set_move(self):
        print("Choose r:rock, p:paper, s:scissors, q:quit")
        # should use lower method on input for input validation
        self.__move = input("Enter your move: ").lower()
    def __is_valid_move(self):
        # need to check if move is valid 
        # by checking move set
        if self.__move not in Human.MOVE_SET:
            print(f"\"{self.__move}\" is an invalid move")
            return False
        else:
            return True
    def __translate_move(self):
        # must change move abbreviations
        # to their counterparts 
        if self.__move not in Human.MOVE_SET:
            if self.__move == "r":
                self.__move = "rock"
            if self.__move == "p":
                self.__move = "paper"
            if self.__move == "s":
                self.__move = "scissors"
            if self.__move == "q":
                self.__move = "quit"
    def set_valid_move(self):
        self.__set_move()
        self.__translate_move()
        while not self.__is_valid_move():
            self.__set_move()
            self.__translate_move()
    def get_move(self):
        return self.__move
    def add_win(self):
        self.__wins += 1
    def add_tie(self):
        self.__ties += 1
    def add_loss(self):
        self.__losses += 1
    def display_stats(self):
        print(f"Stats:\nLost {self.__losses}\nWon {self.__wins}\nTies {self.__ties}\nHave a good one!")
    # refactor: removed increment methods
    # b/c they were unused



