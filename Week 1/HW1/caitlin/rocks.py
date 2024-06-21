# Prompting players
print("Welcome to Rock Paper Scissors. If you don't know how to play, you're dumb but I will help you regardless.")
print("Each player gets to choose one action to shoot. Type rock, paper, or scissors when prompted.")

# best of 3 game
p1wins = 0
p2wins = 0
maxgames = 3
for i in range(0, maxgames):
    p1 = input("Player 1 shoots... ")
    while p1 != 'rock' and p1 != 'paper' and p1 != 'scissors':
        print("I already told you how to play the game, try again.")
        p1 = input("Player 1 shoots... ")
    p2 = input("Player 2 shoots... ")
    while p2 != 'rock' and p2 != 'paper' and p2 != 'scissors':
        print("I already told you how to play the game, try again.")
        p2 = input("Player 2 shoots... ")

    # Who wins?
    # Is it a tie?
    if p1 == p2:
        print("It's a tie! You both suck.")

    # rock and paper
    elif (p1 == 'rock' or p2 == 'rock') and (p1 == 'paper' or p2 == 'paper'):
        print("Paper beats rock.")
        if p1 == 'paper':
            print("Player 1 wins!")
            p1wins += 1
        else:
            print("Player 2 wins!")
            p2wins += 1

    # rock and scissors
    elif (p1 == 'rock' or p2 == 'rock') and (p1 == 'scissors' or p2 == 'scissors'):
        print("Rock beats scissors.")
        if p1 == 'rock':
            print("Player 1 wins!")
            p1wins += 1
        else:
            print("Player 2 wins!")
            p2wins += 1

    # scissors and paper
    elif (p1 == 'paper' or p2 == 'paper') and (p1 == 'scissors' or p2 == 'scissors'):
        print("Scissors beats paper.")
        if p1 == 'scissors':
            print("Player 1 wins!")
            p1wins += 1
        else:
            print("Player 2 wins!")
            p2wins += 1
        
    # score
    print("The score is P1:", p1wins, "vs P2:", p2wins)

    # is there a winner yet?
    if p1wins == 2 or p2wins == 2:
        break
if p1wins == p2wins:
    print("You tied, idiots.")
elif p1wins > p2wins:
    print("Congrats Player 1, you win!")
else:
    print("Congrats Player 2, you win!")