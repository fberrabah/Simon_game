class Player ():
    
    def __init__(self): 
        """contructor with attribut name and score"""
        self.name = None  
        self.score = 0 

    def start(self):
        """ Ask name at player and loop if dont inform good name """
        name = input("Veuillez entrer votre nom pour jouer :")
        while self.checkstart(name) is False:
            name = input("Veuillez entrer votre nom pour jouer :")
        self.name = name
        print("Bonne chance {}".format(name))

    def checkstart(self, name):
        """ Verify name and return True or False"""
        if len(name) > 1 and len(name) < 15 :
            return True
        else : 
            return False
    




    
