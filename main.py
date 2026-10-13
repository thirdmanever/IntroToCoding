import random
import time
from colorama import Fore, init
import os 
init()
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
clearConsole()

score = 10 

def win_game():
    # Use the 'global' keyword so Python knows to change the variable outside this function
    global score 
    
    # 2. Multiply the variable by 2
    score *= 2
    print(f"You won! Your new score is: {score}")

# Testing the code
print(f"Starting score: {score}")
win_game()  # Multiplies by 2 -> 20
win_game()  # Multiplies by 2 -> 40
