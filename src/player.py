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
	
	def reset_player(self):
		self._bet_stack = 0
		self._hand = Hand([])

	def receive_card(self, card):
		self._hand.add_card(card)

	def get_hand(self):
		return self._hand
	
	def get_stack(self):
		return self._personal_stack
	
	def give_chips(self, chips):
		self._personal_stack += chips

	def take_chips(self, chips):
		if self._stack >= chips:
			self._stack -= chips
		else:
			raise ValueError("Player cannot have negative chips")
		
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

	def display_player(self):
		print("--------------------")
		print(f"      {self}")
		print("--------------------")
		for card in self.get_hand():
			print(f"{card}")
		print(f"Score: {self.get_hand().get_hand_value()}")
		print(f"Bet: ${self.get_bet_stack()}")
		print()

	def turn(self, round):
		print(f"{self}, your hand is currently worth {self.get_hand().get_hand_value()} points:")
		if round == 1:
			print("(d)ouble down")
		print("(h)it")
		print("(s)tand")
		while True:
			player_choice = input(":")
			# if the player chooses to either hit or stand, just return their choice
			if player_choice in ['h', 's']:
				return player_choice
			# if the player chooses to double down, A: it must be the first round of action, and B: they must have enough chips left to double their bet
			elif round == 1 and player_choice == "d" and (2 * self.get_bet_stack()) <= self.get_stack():
				return player_choice
			elif round == 1 and player_choice == "d" and (2 * self.get_bet_stack()) > self.get_stack():
				print("You cannot double down, you don't have enough chips")
			# if the player inputs an invalid option, prompt them to try again
			else:
				print("Invalid input, please try again")
		