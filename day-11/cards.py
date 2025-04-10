import random

def create_deck():
    """ Create 52 cards standar deck. """
    suits = ['♣', '♦', '♥', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def shuffle_deck(deck):
    """ Shuffle deck. """
    random.shuffle(deck)

def deal_card(deck):
    """ Deal a deck card. """
    return deck.pop()