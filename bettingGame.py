import random
import time
from colorama import Fore, init
import os

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
clearConsole()
init()
# Fore.RED to make text red
# BACK.RESET to make text black
money = int(10)
print ("You have 10 chances to make 1000 $$$")
time.sleep(2)
clearConsole()
print("Go!")
time.sleep(1)
clearConsole()

win = True
lose = False
print("loading...")
for i in range(10):   
    time.sleep(2)
    clearConsole()


    remaining = 10 - i
    print(f"Chances spent:{i} | chances left: {remaining}")
    print (f"$$$ = ({money})")
    roulette = ["red","blue"]
    ans = random.choice(roulette)
    Red = Fore.RED + "Red"
    Or = Fore.RESET + "or" 
    Black = Fore.BLUE + "Blue"
    space = Fore.RESET + ")"
    choice = input(f"What color do you want to bet on? ({Red} {Or} {Black}{space}\n")
    Fore.RED + "Red" + Fore.RESET + "or" 

    for i in range(1,100):
        clearConsole()
        rand = random.randint(1,48)
    
    if rand%2 == 1:
        print(Fore.RED + str(rand))
    else:
        print(Fore.BLUE + str(rand))
    
    if ans == choice:
        print("Win")
        money *=2
    else:
       print("Lose")
       money *=2    
    print(Fore.RESET)
print ("you lose  :(")
if money == 100:
    clearConsole()
    Print ("you win! :D")
    time.sleep(10)
    clearConsole()


