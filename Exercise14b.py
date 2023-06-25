import random

def game(player, computer)
   if  player == computer:
    print("A Draw!")
    player_input = input("0 =Rock, 1=Paper, 2=Scissors")
    computer_input = random.choice([0,1,2])
    RPS = {0: "Rock", 1: "Paper", 2:"Scissors"}
    print("The computer played", RPS.get(computer_input))