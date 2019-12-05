class Player ():
    
    def __init__(self): #constructor
        self.name = None  #dont know name of player
        self.score = 0 #start with 0 points

    def start(self):
        name = input("Veuillez entrer votre nom pour jouer :")
        while self.checkstart(name) is False:
            name = input("Veuillez entrer votre nom pour jouer :")
        self.name = name
        print("Bonne chance {}".format(name))
        print("C'est partie le jeu commence!!")

    def checkstart(self, name):
        if len(name) > 1 and len(name) < 15 :
            return True
        else : 
            return False




    
