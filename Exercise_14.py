import random
#using fuctions to generate random rock/paper/scissors

#my attempt, could get 0,1,2 identified but couldnt get rest to work, had to use google for help
#and adjust to my needs
#while True :
    #Take input from the user
    #player = str(input("Enter either (0 for Rock, 1 for Paper, 2 for Scissors):"))
    #RPS = [0,1,2]
   # print("You Chose:" + (player))

    #computer makes a random choice
    #computer = random.choice(RPS)
    #show what computer played
    #RPS_dict = {0:"Rock", 1:"Paper", 2:"Scissors"}
    #print("The computer played", RPS_dict.get(computer))
    #making parameters of game

def game(player, computer):
     if player == computer:
         print("Game Tied!")
     else:
         if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and  computer == 1):
              print("You Win!")
         else:
              print("Computer wins!")
def choice(x):

        if x == 0:
            y = "Rock"
        elif x == 1:
            y = "Paper"
        elif x == 2:
            y = "Scissors"
        return y
playing = True
while playing == True:
        player_input = int(input("0 for Rock, 1 for Paper, 2 for Scissors:"))
        print("You Chose:" + choice(player_input))
        computer_input = random.choice([0,1,2])
        print("Computer Chose:" + choice(computer_input))
        game(player_input, computer_input)
        restart = int(input("Enter 7 to play again or 8 to Quit:"))
        if restart == 8:
            playing = False

       # print(game(player, computer))
    #ask for an input
    #again = input("Play again? n for no, y for yes:")

