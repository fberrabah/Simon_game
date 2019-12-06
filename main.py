from player import Player
from sequence import Sequence
from controller import Controller

if __name__ == "__main__":
    
    controller = Controller()
    controller.controller_initialise()
    
                
    while True :    
        controller.computer_play()
        result = controller.player_play()
        if result == False :
            controller.replay()
    # controller.gamer()
    
   
