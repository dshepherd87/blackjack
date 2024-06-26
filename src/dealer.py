from deck import Deck
from hand import Hand
from card import Card

class Dealer:
    def __init__(self):
        self._deck = Deck()
        self._hand = Hand([])

    def shuffle_deck(self):
        self._deck.shuffle()

    def receive_card(self, card):
        self._hand.add_card(card)

    def deal_card(self):
        return self._deck.deal_card()
    
    def show_hand(self):
        return self._hand