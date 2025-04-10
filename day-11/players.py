def calculate_hand_value(hand):
    """ Calculate the total value of the hand, taking in account the Ace as 1 or 11. """
    value = 0
    ace_count = 0

    for card in hand:
        rank, suit = card
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            value += 11
            ace_count += 1
        else:
            value += int(rank)

    # Adjust Ace values if is it necessary
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    
    return value

def is_busted(hand):
    """ Return true if the player has more than 21 points """
    return calculate_hand_value(hand) > 21
    

def show_hand(player, hand, is_dealer=False):
    """Show cards from player (and visible card from the dealer if it is necessary)"""
    if is_dealer:
        print(f"Dealer's hand: [{hand[0]}] and [Hidden]")
    else:
        print(f"{player}'s hand: [{', '.join(map(str, hand))}]")