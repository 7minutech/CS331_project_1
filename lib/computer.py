"""random provides the computer a way to choose a move"""
import random as rand
class Computer:
    """Class representing a computer player for rock paper scissors"""
    # style: capitalized MOVE_SET to show it's a constant
    __MOVE_SET = ["rock","paper", "scissors"]
    def __init__(self):
        self.__move  = ""
        self.__wins = 0
        self.__losses = 0
        self.__ties = 0
    def set_move(self):
        self.__move = rand.choice(Computer.__MOVE_SET)
    def get_move(self):
        return self.__move
    def add_win(self):
        self.__wins += 1
    def add_tie(self):
        self.__ties += 1
    def add_loss(self):
        self.__losses += 1
    

    