import random 

print("Let's play Rock Paper Scissors \n"
"choose R for rock \n"
"choose p for paper \n"
"choose S for scissors \n")

while True:
    game_options = ["R","S","P"]
    cpu = random.choice(game_options)
    player = None

    while player not in game_options:

        player = input("what do you choose: ")
        if player not in game_options:
            print("Invalid input, try again")
        else:
            print("Player:", player , "CPU:",cpu) 
        if player == cpu:
            print("It is a tie")
            continue
        elif player == "R":
            if cpu == "S":
                print("Rock beats Scissors , You win")
            if cpu == "P":
                print("paper beats rock, You lose")
        elif player == "S":
            if cpu == "P":
                print("Scissors beats paper, you win")
            if cpu == "R":
                print("rock beats scissors, you lose")
        elif player == "P":
            if cpu == "S":
                print("Scissors beats paper, You lose ")
            if cpu == "R":
                print("paper beats rock, you win")
        break
    