import random as rand
class Computer:
    # style: capitalized MOVE_SET to show it's a constant
    MOVE_SET = ["rock","paper", "scissors"]
    def __init__(self):
        self.__move  = ""
        self.wins = 0
        self.losses = 0
        self.ties = 0
    def set_move(self):
        self.__move = rand.choice(Computer.MOVE_SET)
    def get_move(self):
        return self.__move
    

    