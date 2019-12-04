class Player ():
    
    def __init__(self):
        self.name = None 
        self.score = 0

    def start(self):
        name = input("Veuillez entrer votre nom pour jouer :")
        while self.checkstart(name) is False:
            name = input("votre nom")
        self.name = name
        
    def checkstart(self, name):
        if len(name) > 1 and len(name) < 15 :
            return True
        else : 
            return False
