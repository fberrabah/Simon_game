from random import *
import time
import os

#os.system('cls' if os.name == 'nt' else 'clear')
 
class Sequence ():

    def __init__(self):
        
        self.stocknumber = []
        self.sleep = None
        self.randint = None

    def display_stocknumber(self):
        """ Display all numbers in stocknumbers """
        for number in self.stocknumber:
            print(number)
            time.sleep(3)
            os.system("clear")
        

    def add_number(self):
        self.stocknumber.append(randint(1,50))

        

    
