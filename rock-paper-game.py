import random
try :
    game = ["rock", "paper", "scissors"]
    player = None
    while player not in game :
        player = input("Enter your choice: rock, paper or scissors: ").lower()
    
    computer = random.choice(game)

    print(f"computer = {computer}")
    print(f"Player = {player}")

    if player == computer:
        print("It's a tie")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins")
        else:
            print("Computer wins")
    elif player == "paper":
        if computer == "scissors":
            print("Computer wins")
        else:
            print("Player wins")
    elif player == "scissors":
        if computer == "rock":
            print("Computer wins")
        else:
            print("Player wins")
except ValueError:
    print("Invalid input")
