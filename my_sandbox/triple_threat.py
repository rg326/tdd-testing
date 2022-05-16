#Triple Threat - Original Card Game!

# Each player (you and computer) starts with no cards (initialize count to 0?)

# Each player picks three cards a turn. The player with the higher sum of cards (QJK = +10), gets to discard their hand.

# If doubles are picked (ie: two of the same cards), the player gets an extra turn. If the sum of the hand is larger than the other player, they also get to discard that hand. If not, the deck is held over for the next round.

# The game continues until the deck is empty. The person with the least amount of cards left is the winner.

# Build Notes
# Attempt to store deck using a dictionary instead or an array, in order to assign specific values to each type of card
# Added test code to work with alt solution
# Might go with array and use a switch statement to assign value instead

import random


def triple_threat():
	card_deck = {
		'1h': 1,
		'1d': 1,
		'1c': 1,
		'1s': 1,
		'2h': 2,
		'2d': 2,
		'2c': 2,
		'2s': 2,
		'3h': 3,
		'3d': 3,
		'3c': 3,
		'3s': 3,
		'4h': 4,
		'4d': 4,
		'4c': 4,
		'4s': 4,
		'5h': 5,
		'5d': 5,
		'5c': 5,
		'5s': 5,
		'6h': 6,
		'6d': 6,
		'6c': 6,
		'6s': 6,
		'7h': 7,
		'7d': 7,
		'7c': 7,
		'7s': 7,
		'8h': 8,
		'8d': 8,
		'8c': 8,
		'8s': 8,
		'9h': 9,
		'9d': 9,
		'9c': 9,
		'9s': 9,
		'10h': 10,
		'10d': 10,
		'10c': 10,
		'10s': 10,
		'jh': 3,
		'jd': 3,
		'jc': 3,
		'js': 3,
		'qh': 3,
		'qd': 3,
		'qc': 3,
		'qs': 3,
		'kh': 3,
		'kd': 3,
		'kc': 3,
		'ks': 3,
		'jo': 10,
		'jo': 10
	}
	
	
	
	my_turn = random.choice(list(card_deck))
	computer = random.choice(list(card_deck))
	
	#print(my_turn)
	#print(computer)
	
	for x,y in card_deck:
		print(card_deck[x])
	
	
	
triple_threat()


''' import random
card_points =['A','K','Q','J','2','3','4','5','6','7','8','9','10']
card_signs =['Heart','CLUB','DIAMOND','SPADE']
random_point = random.choice(card_points)
random_sign = random.choice(card_signs)
random_card = random_point,random_sign
print(random_card)

	def triple_threat():
	card_deck = ['1h','1d','1s','1c','2h','2d','2s','2c','3h','3d','3s','3c','4h','4d','4s','4c','5h','5d','5s','5c','6h','6d','6s','6c','7h','7d','7s','7c','8h','8d','8s','8c','9h','9d','9s','9c','10h','10d','10s','10c','Jh','Jd','Js','Jc','Qh','Qd','Qs','Qc','Kh','Kd','Ks','Kc','Jo1','Jo2']
	my_turn = random.sample(card_deck, 3)
	computer = random.sample(card_deck, 3)
	
		

	
			
					
									
triple_threat()'''


