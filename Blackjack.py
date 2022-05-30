############### Blackjack Project #####################

############### Our Blackjack House Rules #################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

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

#from replit import clear
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #11 is the Ace.
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #returning 0 instead of the actual score. 0 will represent a blackjack in my game.

    if 11 in cards and sum(cards ) > 21:
        cards.remove(11)
        cards.append(1)
    #If the score is already over 21, remove the 11 and replace it with a 1
        
    return sum(cards)

# Comparing scores
def compare(user_score, computer_score):
    """Compares the scores between User and Computer"""
    if user_score == computer_score:
        return "DRAW :/"
    elif computer_score == 0:
        return "LOSE, Opponent has BlackJack :O"
    elif user_score == 0:
        return "WIN, you have a BlackJack =)"
    elif user_score > 21:
        return "You went over, you LOSE :("
    elif computer_score > 21:
        return "Opponent went over, you WIN =D"
    elif user_score > computer_score:
        return "You WIN =D"
    else:
        return "You LOSE :("
    
def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f' Your cards: {user_cards}, current score: {user_score}')
        print(f" Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            #If the game has not ended, ask the user if they want to draw another card.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
         
    
    #Once the user is done, it's time to let the computer play. The computer should keep drawing cards 
    #as long as it has a score less than 17.
    while computer_score != 0 and computer_score > 17:
        computer_cards.append(deal_card())
        computer_score =  calculate_score(computer_cards)
    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BLACKJACK? Type 'y' or 'n': ") == 'y':
    #clear()
    play_game()