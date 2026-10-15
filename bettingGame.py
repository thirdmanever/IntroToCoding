import random
import time
from colorama import Fore, init
import os
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
clearConsole()
init()
money = int(10)
print ("   _____     ")
print ("  /  1  \     ")
print (" | 4   2 |    ")
print ("  \__3__/     ")
while True:

    print (f"$$$ = ({money})")
    roulette = ["1","2","3","4"]
    ans = random.choice(roulette)
    choice = input("What number do you want to bet on? (1,2,3,4)\n")
    clearConsole()
    for i in range(5):
        print ("   _____     ")
        print ("  /  o  \     ")
        print (" | 4 | 2 |    ")
        print ("  \__3__/     ")

        time.sleep(.1)
        clearConsole()

        print ("   _____     ")
        print ("  /  1  \     ")
        print (" | 4 / 2 |    ")
        print ("  \__3__/     ")

        time.sleep(.1)
        clearConsole()

        print ("   _____     ") 
        print ("  /  1  \     ")
        print (" | 4 - o |    ")
        print ("  \__3__/     ")

        time.sleep(.1)
        clearConsole()

        print ("   _____     ")
        print ("  /  1  \     ")
        print (" | 4 \ 2 |    ")
        print ("  \__3__/     ")

        time.sleep(.1)
        clearConsole()

        print ("   _____     ")
        print ("  /  1  \     ")
        print (" | 4 | 2 |    ")
        print ("  \__o__/     ")

        time.sleep(.1)
        clearConsole()

        print ("   _____     ")
        print ("  /  1  \     ")
        print (" | 4 / 2 |    ")
        print ("  \__3__/     ")

        time.sleep(.1)
        clearConsole()

        print ("   _____     ") 
        print ("  /  1  \     ")
        print (" | o - 2 |    ")
        print ("  \__3__/     ")

        time.sleep(.1)
        clearConsole()

        print ("   _____     ")
        print ("  /  1  \     ")
        print (" | 4 \ 2 |    ")
        print ("  \__3__/     ")

        time.sleep(.1)
        clearConsole()
    rand = random.randint(1,4)
    if ans == choice:
        print("Win")
        money *=2
    else:
        print("Lose")
        money /=2    
