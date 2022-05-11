#Triple Threat - Original Card Game!

# Each player (you and computer) starts with no cards (initialize count to 0?)

# Each player picks three cards a turn. The player with the higher sum of cards (QJK = +10), gets to discard their hand.

# If doubles are picked (ie: two of the same cards), the player gets an extra turn. If the sum of the hand is larger than the other player, they also get to discard that hand. If not, the deck is held over for the next round.

# The game continues until the deck is empty. The person with the least amount of cards left is the winner.

import random

def triple_threat():
	card_deck = ['1h','1d','1s','1c','2h','2d','2s','2c','3h','3d','3s','3c','4h','4d','4s','4c','5h','5d','5s','5c','6h','6d','6s','6c','7h','7d','7s','7c','8h','8d','8s','8c','9h','9d','9s','9c','10h','10d','10s','10c','Jh','Jd','Js','Jc','Qh','Qd','Qs','Qc','Kh','Kd','Ks','Kc','Jo1','Jo2']
	my_turn = random.sample(card_deck, 3)
	computer = random.sample(card_deck, 3)
	
		
	
	
			
					
									
triple_threat()



