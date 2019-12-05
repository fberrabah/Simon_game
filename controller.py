from player import Player
from sequence import Sequence
import sys #for quit program

class Controller():
    def __init__(self):
        """ objet player and sequence call attribut """
        self.player = Player()
        self.sequence = Sequence()
    
    def controller_initialise(self):
        """objet player call attribut """
        self.player.start()
        
    def computer_play(self):
        """ call objet with methode """
        self.sequence.add_number()
        self.sequence.display_stocknumber()

    def player_play(self): 
        """ verify answer and list of stocknumber """
        for number in self.sequence.stocknumber:
            answer = input("Veuillez entrez votre nombre :")
            try:
                answer = int(answer)     
            except ValueError:
                print("vous avez perdu vous n'avez pas saisi de nombre")
            if answer != number:
                return False        

        
    def replay(self):
        """answer player if he want replay"""
        print("Vous avez perdu!!")
        while True: # condition for player if want replay
            replay = input("Voulez-vous rejouer? oui/non ").lower() #.lower for translate upper in lower
            if replay == "oui": #if say yes 
                self.sequence.stocknumber = []
                break
            elif replay == "non":
                print("A bientôt.")
                sys.exit() #for exit program 
            else:
                print("C'est oui ou non!!") #if answer are not oui ou non 