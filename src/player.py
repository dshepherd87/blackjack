from hand import Hand
from validators import input_integer

class Player:
	def __init__(self, name, stack):
		self._name = name
		self._personal_stack = stack
		self._bet_stack = 0
		self._hand = Hand([])

	def __repr__(self):
		return self._name
	
	def receive_card(self, card):
		self._hand.add_card(card)

	def get_hand(self):
		return self._hand
	
	def get_stack(self):
		return self._personal_stack

	def give_chips(self, chips):
		self._stack += chips

	def take_chips(self, chips):
		if self._stack >= chips:
			self._stack -= chips
		else:
			raise Exception("Player cannot go negative on stack")
		
	def place_bet(self, bet_amount):
		if bet_amount <= self._personal_stack:
			self._bet_stack += bet_amount
			self._personal_stack -= bet_amount
			return True
		else:
			raise ValueError("Bet is too large, you cannot bet more than you have")

	def get_bet_stack(self):
		return self._bet_stack

	def update_bet_stack(self, new_amount):
		self._bet_stack = new_amount

	def win_bet(self):
		self._personal_stack += self._bet_stack
		self._bet_stack = 0

