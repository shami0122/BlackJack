import random
import os

############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.



def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(nums):
    score = 0
    for num in nums:
        score += num
    return score


def game():
    player_cards = []
    opponent_cards = []
    continue_game = True

    for i in range(2):
        player_cards.append(deal_cards())
        opponent_cards.append(deal_cards())
    
    player_score = calculate_score(player_cards)
    opponent_score = calculate_score(opponent_cards)

    if opponent_score == 21:
        print("You lose, Opponent has a BlackJack!")
        exit
    elif player_score == 21:
        print("You win via BlackJack!")
        exit

    print("\tYour Cards: {cards}, current score: {score}".format(cards = player_cards, score = player_score))
    print("\tComputers first card: {card}".format(card = opponent_cards[0]))

    while continue_game == True:
        decision = input("Type 'y' to get another card, type'n' to pass: ").upper()
        if decision != 'Y':
            continue_game = False
            continue


        

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)
print("""---------------------------------------------------------------
Welcome to the Game of BlackJack! 
---------------------------------------------------------------""")
start_game = input("If you want to start a new game, type 'y' or 'n to exit the game: ").upper()
if(start_game == "Y"):
    os.system('clear')
    print(logo)
    game()
else:
    exit

