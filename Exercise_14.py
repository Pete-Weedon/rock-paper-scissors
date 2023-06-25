import random
#using fuctions to generate random rock/paper/scissors

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
         if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and  computer == 2):
              print("You win!")
         else:
              print("Computer wins!")
def choice(x):
        y = None
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
