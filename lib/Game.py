from colorama import Fore
from .human import Human
from .computer import Computer
import time
import sys
class Game:
    # style: added constants for clarity used inside declare winner method
    PLAYER_1_WIN = 1
    PLAYER_2_WIN = 2

    CHECK_IF_PLAYER_ONE = 1
    CHECK_IF_PLAYER_TWO = 2
    ROUNDS = 3
    """Game class handles prompting and win/loss"""
    def __init__(self):

        #set to null as players aren't selected at start
        self.player_1 = None
        self.player_2 = None

        self.players = 0
        self.winner = 0
        self.active = True
        # feat: added round
        # b/c need to check when the 3rd round has occurred
        self.round = 0
    
    def starting_prompt(self):
        """Handles initial prompting"""
    
        #Initial prompt loop
        while self.active:
            # style: combined print and input for clarity and added best out of 3
            data = input("Welcome To rock paper scissors!\nWould you like to play best out of 3? (Y/N)\n")
            if data.upper() == 'Y' or data.upper() == "YES":
                # style: combined print and input for clarity
                self.players = input("\nPlease make a selection:\nOne player (1)\nTwo players (2)\n")
                try:
                    self.players = int(self.players)
                    if self.players == 1 or self.players == 2:
                        return
                    else:
                        print("Invalid input select 1 or 2")
                except:
                    print("Cannot enter letters")
            
            elif data.upper() == 'N' or data.upper() == "NO":
                print("Good bye!")
                self.active = False
            else:
                print("input invalid")
    # feat: shows a count down before the first move is played 
    def count_down(self):
        # style: time before round starts is longer
        # b/c it lets the user see the results of the previous round easier
        time.sleep(1.5)
        print("rock...")
        time.sleep(1)
        print("paper...")
        time.sleep(1)
        print("scissors...")
        time.sleep(1)
        print("shoot!")
        time.sleep(0.5)
    # feat: should display the round to the user after each round
    def display_round(self):
        message = f"\n---Round {self.round}---\n"
        for char in message:
            time.sleep(0.075)
            print(char, end="")
        
        

    def who_won(self):

        """Declares who won, changed name from winner to who_won for clarity"""
        #keeps things shorter/nicer
        move_1 = self.player_1.move
        move_2 = self.player_2.move

        # refactor: Shortened logic for clarity 
        # refactor: Removed the index into first element
        # b/c the move is always the first letter of the move now
        if move_1[0] == 'r' and move_2[0] == 's' or move_1[0] == "p" and move_2[0] == "r" or move_1[0] == "s" and move_2[0] == "p":
            self.player_1.wins +=1
            self.player_2.losses +=1
            self.winner = 1
            return 
        elif move_1[0] == move_2[0]:
            self.player_1.ties += 1
            self.player_2.ties += 1
            self.winner = 0
            return 
        else:
            self.player_1.losses +=1
            self.player_2.wins +=1
            self.winner = 2
            return 
    def ending_prompt(self):
       
        while self.active:
            answer =  input("Would you like to play again? (Y/N):")
         
            if self.players == Game.CHECK_IF_PLAYER_ONE:
                if answer.lower() == 'n' or answer.lower() == 'no':
                    print(f"Stats:\nLost {self.player_1.losses}\nWon {self.player_1.wins}\nTies {self.player_1.ties}\nHave a good one!")
                    self.active = False
                    return
                elif answer.lower() == 'y' or answer.lower() == 'yes':
                    self.active = True
                    return 
            if self.players == Game.CHECK_IF_PLAYER_TWO:
                if answer.lower() == 'n' or answer.lower() == 'no':
                    print(f"Stats Player 1:\nLost {self.player_1.losses}\nWon {self.player_1.wins}\nTies {self.player_1.ties}")
                    print(f"\nStats Player 2:\nLost {self.player_2.losses}\nWon {self.player_2.wins}\nTies {self.player_2.ties}")
                    self.active = False
                    return
                elif answer.lower() == 'y' or answer.lower() == 'yes':
                    self.active = True
                    return 
    def declare_winner(self):
        #Changes prompt based on player count
        # feat: added colored text depending the result
        if self.players == Game.CHECK_IF_PLAYER_ONE:
            if self.winner == Game.PLAYER_1_WIN:
                print(f"{Fore.GREEN}You win{Fore.WHITE}")
            elif self.winner == Game.PLAYER_2_WIN:
                print(f"{Fore.RED}You lost{Fore.WHITE}")
            else:
                print(f"{Fore.YELLOW}It was a tie!{Fore.WHITE}")
        else:
            if self.winner == Game.PLAYER_1_WIN:
                print(f"{Fore.GREEN}Player 1 wins!{Fore.WHITE}") 
            elif self.winner == Game.PLAYER_2_WIN:
                print(f"{Fore.GREEN}Player 2 wins!{Fore.WHITE}")
            else:
                print(f"{Fore.YELLOW}It was a tie!{Fore.WHITE}")
    # feat: can quit out of program during the prompt for move
    def has_quit(self):
        if self.player_1.move == "quit" or self.player_2.move == "quit":
            if self.players == 1:
                print(f"Stats:\nLost {self.player_1.losses}\nWon {self.player_1.wins}\nTies {self.player_1.ties}\nHave a good one!")
                self.active = False
                sys.exit()
            else:
                print(f"Stats Player 1:\nLost {self.player_1.losses}\nWon {self.player_1.wins}\nTies {self.player_1.ties}")
                print(f"\nStats Player 2:\nLost {self.player_2.losses}\nWon {self.player_2.wins}\nTies {self.player_2.ties}")
                self.active = False
                sys.exit()
        
    def play(self):       
        """Main loop"""
        self.starting_prompt()
        #creates and sets players according to selection
        if self.players == Game.CHECK_IF_PLAYER_ONE:
            self.player_1 = Human()
            self.player_2 = Computer()
           
        elif self.players == Game.CHECK_IF_PLAYER_TWO:
            self.player_1 = Human()
            self.player_2 = Human()

        while self.players == Game.CHECK_IF_PLAYER_ONE and self.active:            
            self.round += 1
            self.display_round()
            self.count_down()
            #Gets/prompts moves
            self.player_1.set_valid_move()
            self.has_quit()
            self.player_2.set_move()
            self.who_won()
            print (f"\nComputer move: {self.player_2.move}")
            print (f"\nPlayer move: {self.player_1.move}")
            # refactor: avoided repeated code by using method
            self.declare_winner()

            #refactor: avoided repeated code by using method
            if self.round % 3 == 0:
                self.ending_prompt()
        while self.players == Game.CHECK_IF_PLAYER_TWO and self.active:
            self.round += 1
            self.display_round()
            self.count_down()
            #prompts players
            print("Player one, please select a move!")
            self.player_1.set_valid_move()
            self.has_quit()
            print("\nPlayer two, please select a move!")
            self.player_2.set_valid_move()
            self.has_quit()
            
            self.who_won()

            print (f"\nPlayer 1 move: {self.player_1.move}")
            print (f"\nPlayer 2 move: {self.player_2.move}")


            # refactor: avoided repeated code by using method
            self.declare_winner()

            #refactor: avoided repeated code by using method
            if self.round % Game.ROUNDS == 0:
                self.ending_prompt()
    

