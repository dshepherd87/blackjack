from card import Card

# The Hand object is really just a list of Card objects, with some necessary logic added to determine the value of the hand
class Hand:
    def __init__(self, cards=[]):
        self._cards = cards
        self._value = self.get_hand_value()

    def __repr__(self):
        """result = ""
        for card in self._cards:
            result += f"{card} "
        return result"""
        return self._cards
    
    def show_card(self, index):
        return self._cards[index]

    def add_card(self, card):
        self._cards.append(card)

    def get_hand_value(self) -> int:
        value = 0
        cards = sorted(self._cards)

        for card in cards:
            # if the card is a numbered card, it simply has its face value
            if card.get_rank() <= 10:
                value += card.get_rank()
            # Jack, Queen, and King are all worth 10
            elif card.get_rank() > 10 and card.get_rank() < 14:
                value += 10
            # the value of an Ace is situational - it defaults to 11, but if that will make the player bust then it is worth 1 instead
            elif card.get_rank() == 14 and value <= 10:
                value += 11
            elif card.get_rank() == 14 and value > 10:
                value += 1
        return value