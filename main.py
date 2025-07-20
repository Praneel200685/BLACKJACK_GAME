from art import logo
import random

print(logo)

# Function to deal a card
def deal_cards():
    list_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(list_of_cards)

# Function to calculate score
def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Represents a Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Function to compare scores
def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a Draw"
    elif c_score == 0:
        return "You lose, opponent has a Blackjack"
    elif u_score == 0:
        return "You win, you got a Blackjack"
    elif u_score > 21:
        return "You lose, you went over 21"
    elif c_score > 21:
        return "You win, opponent went over 21"
    elif u_score > c_score:
        return "You win, closer to 21"
    else:
        return "You lose"

# Start the game
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            q = input("Do you want another card? Type 'y' or 'n': ")
            if q == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    # Computer's turn: draw until score is at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calc_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Ask user if they want to play
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()