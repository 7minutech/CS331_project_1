class Human:
    # style: capitalized MOVE_SET to show it's a constant
    # feat: added quit to move set to allow user to quit out of program
    MOVE_SET = ["rock","paper", "scissors", "quit"]
    def __init__(self):
        self.move = ""
        self.wins = 0
        self.ties = 0
        self.losses = 0
    def set_move(self):
        print("Choose r:rock, p:paper, s:scissors, q:quit")
        # should use lower method on input for input validation
        self.move = input("Enter your move: ").lower()
    def is_valid_move(self):
        # need to check if move is valid 
        # by checking move set
        if self.move not in Human.MOVE_SET:
            print(f"\"{self.move}\" is an invalid move")
            return False
        else:
            return True
    def translate_move(self):
        # must change move abbreviations
        # to their counterparts 
        if self.move not in Human.MOVE_SET:
            if self.move == "r":
                self.move = "rock"
            if self.move == "p":
                self.move = "paper"
            if self.move == "s":
                self.move = "scissors"
            if self.move == "q":
                self.move = "quit"
    def set_valid_move(self):
        self.set_move()
        self.translate_move()
        while not self.is_valid_move():
            self.set_move()
            self.translate_move()
    # refactor: removed increment methods
    # b/c they were unused



