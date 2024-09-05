import random as rand
class Computer:
    # style: capitalized MOVE_SET to show it's a constant
    MOVE_SET = ["rock","paper", "scissors"]
    def __init__(self):
        self.__move  = ""
        self.__wins = 0
        self.__losses = 0
        self.__ties = 0
    def set_move(self):
        self.__move = rand.choice(Computer.MOVE_SET)
    def get_move(self):
        return self.__move
    def get_wins(self):
        return self.__wins
    def add_win(self):
        self.__wins += 1
    def get_ties(self):
        return self.__wins
    def add_tie(self):
        self.__ties += 1
    def get_losses(self):
        return self.__losses
    def add_lossn(self):
        self.__losses += 1
    

    