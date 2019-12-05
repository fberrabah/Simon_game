from player import Player
from sequence import Sequence
import sys

class Controller():
    def __init__(self):
        self.player = Player()
        self.sequence = Sequence()
    
    def controller_initialise(self):
        self.player.start()
        
    def computer_play(self):
        self.sequence.add_number()
        self.sequence.display_stocknumber()

    def player_play(self): 
        """verify answer and list of stocknumber"""
        for number in self.sequence.stocknumber:
            answer = input("Veuillez entrer votre nombre :")
            try:
                answer=int(answer)     
            except ValueError:
                print("vous n'avez pas saisi de nombre")
                continue
            if answer != number:
                return False        

        

    def replay(self):
        print("Vous avez perdu!!")
        while True: # condition for player if want replay
            replay=input("Voulez-vous rejouer? oui/non ").lower() #.lower for translate upper in lower
            if replay == "oui": #if say yes 
                self.sequence.stocknumber = []
                break
            elif replay == "non":
                print("A bientôt.")
                sys.exit() #for exit program 
            else:
                print("C'est oui ou non!!") #if answer are not oui ou non 