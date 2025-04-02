#Generating all possible dice rolls
import random

def determine_winner(p1_sum, p2_sum, di):
    p1_probability = di[str(p1_sum)]
    p2_probability = di[str(p2_sum)]
    
    if p1_probability < p2_probability:
        return "Player 1"
    elif p1_probability > p2_probability:
        return "Player 2"
    else:
        return "Draw"

d1 = [1,2,3,4,5,6]
d2 = [1,2,3,4,5,6]
li = []
for i in d1:
    for j in d2:
        li.append((i,j))
print(li)

#probability calculating

di = {}
for i in range(2,13):
    c = 0
    for j in li:
        if i == j[0]+j[1]:
            c+=1
    di[str(i)] = c/len(li)
print(di)

R = int(input("Enter the number of rounds: "))

player1_wins = 0
player2_wins = 0
draws = 0

for i in range(1, R+1):
        player1_dice1, player1_dice2 = random.randint(1,6), random.randint(1,6)
        player2_dice1, player2_dice2 = random.randint(1,6), random.randint(1,6)
        
        player1_sum = player1_dice1 + player1_dice2
        player2_sum = player2_dice1 + player2_dice2
        
        winner = determine_winner(player1_sum,player2_sum,di)
        if winner == "Player 1":
            player1_wins += 1
        elif winner == "Player 2":
            player2_wins += 1
        else:
            draws += 1
        # Print the result of the round
print(f"\nRound {i} result: {winner}")

# Print the final score
print(f"\nFinal Score:")
print(f"Player 1: {player1_wins}")
print(f"Player 2: {player2_wins}")
print(f"Draws: {draws}")

if player1_wins > player2_wins:
    print('Player 1 wins the game')
elif player1_wins < player2_wins:
    print('Player 2 wins the game')
else :
    print('Its a draw game')

        
        
        
        
        
        
        
        
        
