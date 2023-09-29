import sys
import random
from enum import Enum

class RPS(Enum):
    Rock =1
    Paper = 2
    Scissors =3

value = input('enter.. \n1 for Rock, \n2 for paper, \n3 for scissors: \n')

playerChoice = int(value)

computerChoice = random.choice("123")

computer = int(computerChoice)

if playerChoice < 1 or playerChoice > 3:
    sys.exit("invalid number")

print("Computer choice " + str(RPS(computer)).replace('RPS.',''))
print("Player choice " + str(RPS(playerChoice)).replace('RPS.',''))