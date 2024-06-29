import unittest
from ut.readers import read_csv
from card import Card

class TestCard(unittest.TestCase):
    def test_repr(self):
        test_cases = read_csv('files/cardTestCases.csv')
        for test_case in test_cases:
            test_input = str(Card(int(test_case[0]), test_case[1]))
            base_case = test_case[2]
            self.assertEqual(test_input, base_case)



