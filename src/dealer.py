from deck import Deck
from hand import Hand
from card import Card

class Dealer:
    def __init__(self):
        self._deck = Deck()
        self._hand = Hand([])
        self._stands_on = 17

    def shuffle_deck(self):
        self._deck.shuffle()

    def receive_card(self, card):
        self._hand.add_card(card)

    def deal_card(self):
        return self._deck.deal_card()
    
    def show_hand(self):
        return self._hand
    
    def print_full_hand(self):
        for card in self.show_hand():
            print(card)
    
    def print_first_card(self):
        print(f"{self.show_hand().show_card(0)}")
    
    def display_dealer(self):
        print("--------------------")
        print("       Dealer")
        print("--------------------")     