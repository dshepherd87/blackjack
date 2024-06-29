import unittest
from hand import *
from ut.readers import read_csv

class TestHand(unittest.TestCase):
    def test_hand_value(self):
        test_cases = read_csv('files/handValueCases.csv')
        for test_case in test_cases:
            cards = []
            for i in range(0, len(test_case)-1, 2):
                cards.append(Card(int(test_case[i]), test_case[i+1]))
            hand = Hand(cards)
            self.assertEqual(hand.get_hand_value(),int(test_case[-1]))

