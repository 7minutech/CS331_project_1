import pdb
class Human:
    # style: capitalized MOVE_SET to show it's a constant
    # feat: added quit to move set to allow user to quit out of program
    MOVE_SET = ["rock","paper", "scissors", "quit"]
    def __init__(self):
        self.__move = ""
        print(self.__move)
        self.wins = 0
        self.ties = 0
        self.losses = 0
    def set_move(self):
        print("Choose r:rock, p:paper, s:scissors, q:quit")
        # should use lower method on input for input validation
        self.__move = input("Enter your move: ").lower()
    def is_valid_move(self):
        # need to check if move is valid 
        # by checking move set
        if self.__move not in Human.MOVE_SET:
            print(f"\"{self.__move}\" is an invalid move")
            return False
        else:
            return True
    def translate_move(self):
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
        self.set_move()
        self.translate_move()
        while not self.is_valid_move():
            self.set_move()
            self.translate_move()
    def get_move(self):
        return self.__move
    # refactor: removed increment methods
    # b/c they were unused



