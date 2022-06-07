#Triple Threat - Original Card Game!

# Each player (you and computer) starts with no cards (initialize count to 0?)

# Each player picks three cards a turn. The player with the higher sum of cards (QJK = +10), gets to discard their hand.

# If doubles are picked (ie: two of the same cards), the player gets an extra turn. If the sum of the hand is larger than the other player, they also get to discard that hand. If not, the deck is held over for the next round.

# The game continues until the deck is empty. The person with the least amount of cards left is the winner.

# Build Notes
# Attempt to store deck using a dictionary instead or an array, in order to assign specific values to each type of card
# Added test code to work with alt solution
# Might go with array and use a switch statement to assign value instead

####

# Find a way to take the string of the dict and compare its value to an
# action (Done)
# Use a conditional for each key in dict (not needed)

# Next steps:
# Discard the cards pulled by the winner of each round (delete from deck, and store the cards pulled by the loser in its own deck.
# Problem: Getting Python to recognize global variables, rather than scoping them to each function 
# Conditional in start_game() still has bugs (else not working)
# Might refactor entire code to javascript due to better handling of scoped variables
# Fixed it! Remember to place global variables at the top of the function instead
# Will most likely still refactor to javascript. Each item in the card deck will be its own distinct object ie: {card.title, card.value, card.image}

import random
import time


card_deck = {
	'1 of Hearts': 1,
	'1 of Diamonds': 1,
	'1 of Clubs': 1,
	'1 of Spades': 1,
	'2 of Hearts': 2,
	'2 of Diamonds': 2,
	'2 of Clubs': 2,
	'2 of Spades': 2,
	'3 of Hearts': 3,
	'3 of Diamonds': 3,
	'3 of Clubs': 3,
	'3 of Spades': 3,
	'4 of Hearts': 4,
	'4 of Diamonds': 4,
	'4 of Clubs': 4,
	'4 of Spades': 4,
	'5 of Hearts': 5,
	'5 of Diamonds': 5,
	'5 of Clubs': 5,
	'5 of Spades': 5,
	'6 of Hearts': 6,
	'6 of Diamonds': 6,
	'6 of Clubs': 6,
	'6 of Spades': 6,
	'7 of Hearts': 7,
	'7 of Diamonds': 7,
	'7 of Clubs': 7,
	'7 of Spades': 7,
	'8 of Hearts': 8,
	'8 of Diamonds': 8,
	'8 of Clubs': 8,
	'8 of Spades': 8,
	'9 of Hearts': 9,
	'9 of Diamonds': 9,
	'9 of Clubs': 9,
	'9 of Spades': 9,
	'10 of Hearts': 10,
	'10 of Diamonds': 10,
	'10 of Clubs': 10,
	'10 of Spades': 10,
	'Jack of Hearts': 3,
	'Jack of Diamonds': 3,
	'Jack of Clubs': 3,
	'Jack of Spades': 3,
	'Queen of Hearts': 3,
	'Queen of Diamonds': 3,
	'Queen of Clubs': 3,
	'Queen of Spades': 3,
	'King of Hearts': 3,
	'King of Diamonds': 3,
	'King of Clubs': 3,
	'King of Spades': 3,
	'Joker A': 10,
	'Joker B': 10
}


"""my_turn_1 = random.choice(list(card_deck))
my_turn_2 = random.choice(list(card_deck))
my_turn_3 = random.choice(list(card_deck))
comp_turn_1 = random.choice(list(card_deck))
comp_turn_2 = random.choice(list(card_deck))
comp_turn_3 = random.choice(list(card_deck))"""

"""my_turn_1 = random.sample(card_deck.items(), 1)
my_turn_2 = random.sample(card_deck.items(), 1)
my_turn_3 = random.sample(card_deck.items(), 1)
comp_turn_1 = random.sample(card_deck.items(), 1)
comp_turn_2 = random.sample(card_deck.items(), 1)
comp_turn_3 = random.sample(card_deck.items(), 1)"""

hand = card_deck.keys()

"""my_turn_1 = random.sample(list(hand), 1)
my_turn_2 = random.sample(list(hand), 1)
my_turn_3 = random.sample(list(hand), 1)

comp_turn_1 = random.sample(list(hand), 1)
comp_turn_2 = random.sample(list(hand), 1)
comp_turn_3 = random.sample(list(hand), 1)"""

#Variables
my_deck = {}
comp_deck = {}
my_turn = random.sample(list(hand), 3)
comp_turn = random.sample(list(hand), 3)

my_score = 0
comp_score = 0
my_hand = 0
comp_hand = 0


def play_turn():
	global my_score
	global comp_score
	global my_hand
	global comp_hand
	
	if len(card_deck) == 0:
		if my_score > comp_score:
			print(f"There are no more cards to choose from. Your final score is {my_score}. The computer's score is {comp_score}. You win! Care to play again?")
		elif comp_score > my_score:
			print(f"There are no more cards to choose from. Your final score is {my_score}. The computer's score is {comp_score}. You Lose. Care to play again?")
		elif my_score == comp_score:
			print(f"There are no more cards in the deck. Your final score is {my_score}. The computer's score is {comp_score}. It's a draw! Care to play again?")
	
	
	my_turn = random.sample(list(hand), 3)
	comp_turn = random.sample(list(hand), 3)
	
	print(len(card_deck))
	
	print("It's your turn!'")
	print(my_turn)
	for x in my_turn:
		print(card_deck[x])
		my_hand += card_deck[x]
	#print(my_turn_2)
	#print(my_turn_3)
	
	print("It's the computer's turn!")
	#time.sleep(2)
	print(comp_turn)
	for x in comp_turn:
		print(card_deck[x])
		comp_hand += card_deck[x] 
	#print(comp_turn_2)
	#print(comp_turn_3)
	
	if my_hand > comp_hand:
		print("You win this round! Please discard your hand.")
		for x in my_turn:
			del card_deck[x]
		my_score += 1
		print(f"Your current score is {my_score}. The computer's score is {comp_score}.")
		
	elif comp_hand > my_hand:
		print("You've lost this round. Please hold on to your current cards.")
		for x in comp_turn:
			del card_deck[x]
		comp_score += 1
		print(f"The computer's current score is {comp_score}. Your score is {my_score}.")	
	else:
		print("It's a draw! Please play another turn! Your current score is {my_score}. The computer's score is {comp_score}.")
		play_turn()
		
	
	


#for x in card_deck:
#	print(y)

def start_game():
		print('Hello there! Welcome to Triple Threat! Would you like to play a round?')
		#print('')
		play_game = input('Press Y/y to play, and N/n to get out of here!\n')
		is_gameloop = True
		
		while is_gameloop:
			if play_game is "Y" or "y":
				play_turn()
			elif play_game is "N" or "n":
				is_gameloop = False
			#elif player_input is "N" or "n":
			#	break
			else:
				None
				
			print('Good round! Would you like to continue?')
			cont_game = input()	
			
			if cont_game is "Y" or "y":
				play_turn()
			elif cont_game is "N" or "n":
				is_gameloop = False
			else:
				is_gameloop = False
	

start_game()

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
