import random
import art

def deal_card():
    """function that deals random cards and returns them"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Function that calculates the sum of all cards in a hand, and returs 0 if it's a black jack. Also deals with the exception for aces"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(player_score, comp_score):
    """Function that compares the player score with the computer score and returns de result of the game"""
    if player_score == comp_score:
        return "It's a draw!"
    elif comp_score == 0:
        return"You loose! Computer has a Blackjack!"
    elif player_score == 0:
        return "You win! You have a Blackjack!"
    elif player_score > 21:
        return "You loose! You went over 21!"
    elif comp_score > 21:
        return "You win! Computer went over 21!"
    elif player_score > comp_score:
        return "You win!"
    else:
        return "You lose!"

def play_again():
    """Function that manages the entire game"""
    print(art.logo)
    player_hand = []
    computer_hand = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your hand: {player_hand} - score: {user_score}")
        print(f"Computer hand: [{computer_hand[0]}, *]")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            keep_playing = input("Do you want to draw another card? (y/n)")
            if keep_playing == "y":
                player_hand.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Your hand: {player_hand}")
    print(f"Computer hand: {computer_hand}")
    print(compare_scores(user_score, computer_score))

while input("Do you want to play a game of Blackjack? type 'y' or 'n' ").lower() == "y":
        print("\n" * 20)
        play_again()
