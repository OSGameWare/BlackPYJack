import random
import time
import usrinfo

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

def get_strategy_advice(player_total, dealer_card):
    dealer_value = 10 if dealer_card.value in ['J', 'Q', 'K'] else (
        11 if dealer_card.value == 'A' else int(dealer_card.value))
    
    if player_total >= 17:
        return "Stand"
    elif player_total <= 8:
        return "Hit"
    elif player_total == 11:
        return "Double"
    elif player_total >= 12 and player_total <= 16 and dealer_value >= 7:
        return "Hit"
    elif player_total >= 12 and player_total <= 16:
        return "Stand"
    elif player_total == 10 and dealer_value <= 9:
        return "Double"
    elif player_total == 9 and dealer_value <= 6:
        return "Double"
    else:
        return "Hit"

def calculate_probability(player_total, dealer_card):
    if player_total > 21:
        return 0  # Bust, 0% chance to win
    
    # Basic probability calculation based on dealer's up card
    dealer_value = 10 if dealer_card.value in ['J', 'Q', 'K'] else (
        11 if dealer_card.value == 'A' else int(dealer_card.value))
    
    # Higher probability if dealer might bust
    if dealer_value >= 7:
        return max(0, min(100, (21 - player_total) * 10))
    else:
        return max(0, min(100, (21 - dealer_value) * 8))

def calculate_hand(hand):
    value = 0
    aces = 0

    for card in hand:
        if card.value in ['J', 'Q', 'K']:
            value += 10
        elif card.value == 'A':
            aces += 1
        else:
            value += int(card.value)

    for _ in range(aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1

    return value

def play_game():
    deck = Deck()
    player_hand = []
    dealer_hand = []

    print("\033c")
    # Place bet with chips
    while True:
        try:
            bet = int(input(f"\nYour chips: {usrinfo.chips}\nEnter your bet in chips: "))
            if bet <= usrinfo.chips and bet > 0:
                usrinfo.chips -= bet
                break
            print("Invalid bet amount!")
        except ValueError:
            print("Please enter a valid number!")
    print("\033c")
    # Initial deal
    player_hand.append(deck.deal())
    dealer_hand.append(deck.deal())
    player_hand.append(deck.deal())
    dealer_hand.append(deck.deal())

    while True:
        print("\nDealer's hand:", dealer_hand[0], "[Hidden]")
        print("Your hand:", *player_hand)
        player_total = calculate_hand(player_hand)
        print("Your total:", player_total)
        if usrinfo.show_probability:
            win_chance = calculate_probability(player_total, dealer_hand[0])
            print(f"Estimated win probability: {win_chance:.1f}%", end="")
            if usrinfo.show_strategy:
                strategy = get_strategy_advice(player_total, dealer_hand[0])
                print(f" - Suggested play: {strategy}")
            else:
                print()

        if calculate_hand(player_hand) == 21:
            print("Blackjack! You win!")
            usrinfo.chips += bet * 2.5
            break

        action = input("\nWhat would you like to do? (hit/stand/double): ").lower()
        
        if action == 'double':
            if usrinfo.chips >= bet:  # Check if player has enough chips to double
                usrinfo.chips -= bet
                bet *= 2
                player_hand.append(deck.deal())
                print("\nYour hand:", *player_hand)
                if calculate_hand(player_hand) > 21:
                    print("Bust! You lose!")
                    print("Your final hand:", *player_hand)
                    break
                action = 'stand'  # Force stand after double down
            else:
                print("Not enough money to double down!")
                continue
                
        if action == 'hit':
            player_hand.append(deck.deal())
            if calculate_hand(player_hand) > 21:
                print("\nBust! You lose!")
                print("Your final hand:", *player_hand)
                break
        elif action == 'stand':
            # Dealer's turn
            print("\nDealer's hand:", *dealer_hand)
            while calculate_hand(dealer_hand) < 17:
                dealer_hand.append(deck.deal())
                print("Dealer hits:", dealer_hand[-1])
                time.sleep(1)

            dealer_total = calculate_hand(dealer_hand)
            player_total = calculate_hand(player_hand)

            print(f"\nDealer's total: {dealer_total}")
            print(f"Your total: {player_total}")

            if dealer_total > 21:
                print("Dealer busts! You win!")
                usrinfo.chips += bet * 2  # Original bet + win
            elif dealer_total > player_total:
                print("Dealer wins!")
            elif dealer_total < player_total:
                print("You win!")
                usrinfo.chips += bet * 2  # Original bet + win
            else:
                print("Push!")
                usrinfo.chips += bet  # Return original bet
            break

    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    return play_again == 'yes'

    

