# Prompting players
p1 = input("Player 1 shoots... ")
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
    else:
        print("Player 2 wins!")

# rock and scissors
elif (p1 == 'rock' or p2 == 'rock') and (p1 == 'scissors' or p2 == 'scissors'):
    print("Rock beats scissors.")
    if p1 == 'rock':
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

# scissors and paper
elif (p1 == 'paper' or p2 == 'paper') and (p1 == 'scissors' or p2 == 'scissors'):
    print("Scissors beats paper.")
    if p1 == 'scissors':
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")