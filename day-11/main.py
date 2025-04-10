from cards import create_deck, shuffle_deck, deal_card
from players import calculate_hand_value, is_busted, show_hand

def player_turn(deck, player_hand):
    """ Player's turn logic. """
    while True:
        print("======")
        show_hand('Player', player_hand)
        print("======")
        action = input("Do you want to [h]it or [s]tand? ").lower()
        
        if action == 'h':
            card = deal_card(deck)
            player_hand.append(card)
            print(f"You drew: {card}")
            
            if is_busted(player_hand):
                show_hand('Player', player_hand)
                print("You busted! Game over.")
                return False  # Over 21, Lost
        elif action == 's':
            break
        else:
            print("Invalid choice. Please choose 'h' or 's'.")
    
    return True  # Player chose (stand)

def dealer_turn(deck, dealer_hand):
    """ Dealer's turn logic """
    while calculate_hand_value(dealer_hand) < 16:
        card = deal_card(deck)
        dealer_hand.append(card)
        print(f"Dealer drew: {card}")

def game():
    """ Main Game Loop. """
    deck = create_deck()
    
    shuffle_deck(deck)

    #Initial hands
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    print("♣ ♦ ♥ ♠ Welcome to Blackjack ♠ ♥ ♦ ♣")
    
    # Show initial hands
    show_hand('Dealer', dealer_hand, is_dealer=True)
    show_hand('Player', player_hand)

    # Player's turn
    if not player_turn(deck, player_hand):
        print("You lost!")
        return
    
    # Dealers' turn
    dealer_turn(deck, dealer_hand)
    show_hand('Dealer', dealer_hand)
    
    # Calculate result
    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)
    
    print(f"Your score: {player_score}")
    print(f"Dealer's score: {dealer_score}")
    
    if player_score > 21:
        print("You busted! Dealer wins.")
    elif dealer_score > 21:
        print("Dealer busted! You win.")
    elif player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    game()