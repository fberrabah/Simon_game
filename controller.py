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
        self.difficulty()
        

        
        
    def computer_play(self):
        """ call objet with methode """
        
        self.sequence.add_number()
        self.sequence.display_stocknumber()

    def player_play(self): 
        """ verify answer and list of stocknumber """
        for number in self.sequence.stocknumber:
            answer = input("Veuillez entrer votre nombre :")
            try:
                answer = int(answer)     
            except ValueError:
                print("Vous n'avez pas saisi de nombre")
            if answer != number:
                return False        

        
    def replay(self):
        """answer player if he want replay"""
        print("Vous avez perdu!!")
        while True: # condition for player if want replay
            replay = input("Voulez-vous rejouer? oui/non ").lower() #.lower for translate upper in lower
            if replay == "oui": #if say yes 
                self.sequence.stocknumber = []
                self.difficulty()
                break
            elif replay == "non":
                print("A bientôt.")
                sys.exit() #for exit program 
            else:
                print("C'est oui ou non!!") #if answer are not oui ou non 
    
    def difficulty(self):
            level = input(" ~~~~ Niveau Facile taper : 1    ~~~~ \n ~~~~ Niveau moyen taper : 2     ~~~~ \n ~~~~ Niveau difficile taper : 3 ~~~~ \n Veuillez choisir le niveau de difficulté : ")

            if level == "1" :
                self.sequence.sleep = 3 
                self.sequence.randint = 10
            elif level == "2" : 
                self.sequence.sleep = 2 
                self.sequence.randint = 20
            elif level == "3" :   
                self.sequence.sleep = 1 
                self.sequence.randint = 100
        
            else:
                print("C'est 1, 2 ou 3")
                self.difficulty()
        
            print("C'est partie le jeu commence!!")

            