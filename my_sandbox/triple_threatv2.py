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

#Figuring out how to restore card deck for new game
# Trying to make it work with copy or deepcopy (need to play around with it more)
# Figuring out how to fix random keyerror that appears during iteration of deck

#Look up more pass by value related methods
#Find out why deepcopy isn't working as expected
#Realized card deck is NOT the same copy as starting deck
#Attempted to restore deck with a function
#Find a way to manually deep copy the dict within the function
# populating deck issue is the problem
# working in js might be easier
# found out objects are harder to work with in js compared to dicts in python
# still having difficulty repopulating the deck after game reset


import random
import copy
import time

#THE STARTING DECK
starting_deck = {
	'A of Hearts': 1,
	'A of Diamonds': 1,
	'A of Clubs': 1,
	'A of Spades': 1,
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


#COPYING STARTING DECK BY VALUE TO EMPTY CARD DECK
#card_deck = {}
card_deck = copy.deepcopy(starting_deck)

#Getting the keys of the deck as an array for each hand played
hand = card_deck.keys()


#Variables

#Initializing empty deck for player
my_deck = {}
#Initializing empty deck for computer
comp_deck = {}
my_turn = random.sample(list(hand), 3)
comp_turn = random.sample(list(hand), 3)

#counters for keeping score
my_score = 0 
comp_score = 0

#sum of hand per turn for each player
my_hand = 0
comp_hand = 0

#function to play a turn
def play_turn():
	global hand
	global my_score
	global comp_score
	global my_hand
	global comp_hand
	#global starting_deck
	global card_deck
	
	#picking out 3 cards at random from the keys in hand variable
	my_turn = random.sample(list(hand), 3)
	comp_turn = random.sample(list(hand), 3)
	
	#display remaining cards in card deck
	print(card_deck)
	
	print(f"Cards remaining in deck: {len(card_deck)}")
	
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
	
	#Setting up the conditionals for various win/lose scenarios

	#If player beats computer in a turn
	if my_hand > comp_hand:
		print("You win this round! Please discard your hand.")

		#remove the card from the card deck for each 3 cards and add the value of each card in the hand played to player's score
		for x in my_turn:
			del card_deck[x]
		my_score += 1
		print(f"Your current score is {my_score}. The computer's score is {comp_score}. Please enter 'Y/y' to continue or 'N/n' to leave.")

	#If computer beats player in a turn
	#Do the same for above, but for the computer		
	elif comp_hand > my_hand:
		print("You've lost this round. Please hold on to your current cards. Please press 'Y' or 'y' to continue.")
		for x in comp_turn:
			del card_deck[x]
		comp_score += 1
		print(f"The computer's current score is {comp_score}. Your score is {my_score}. Please enter 'Y/y' to continue or 'N/n' to leave.")	
	else:
		print("It's a draw! Please play another turn! Your current score is {my_score}. The computer's score is {comp_score}. Please enter 'Y/y' to continue or 'N/n' to leave.")
		play_turn()
		

	


#for x in card_deck:
#	print(y)

def start_game():
	#global starting_deck
	#global card_deck
	
	#card_deck = copy.deepcopy(starting_deck)
	#is_gameloop = True
		
	
	print('Hello there! Welcome to Triple Threat! Would you like to play a round?')
	#print('')
	play_game = input('Enter Y/y to play, and N/n to get out of here!\n')
	play_game = play_game.upper()
		
	if play_game == "Y":
		play_turn()
	elif play_game == "N":
		print("Game Over")
		return None
	
	while len(card_deck) > 1:		
		
		cont_game = input('Nice round! Care to try again? Y/N \n')
		cont_game = cont_game.upper()	
		
		
				
		if cont_game == "Y":
			play_turn()
		elif cont_game == "N":
			print("Game Over")
			return None

# function to restore deck on game replay			
def restore_deck():
	global starting_deck
	
	'''card_deck = {
	'A of Hearts': 1,
	'A of Diamonds': 1,
	'A of Clubs': 1,
	'A of Spades': 1,
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
	}'''
	
	card_deck = copy.deepcopy(starting_deck)

def end_game():
	global my_score
	global comp_score
	global my_hand
	global comp_hand
	global card_deck
	global restore_deck
	
	#if len(card_deck) == 0:
	#	print("Game Over")
	
	if len(card_deck) == 0:
		"""print(f"The game is over! Final score is: My score: {my_score}, Computer score: {comp_score}!")"""
		if my_score > comp_score:
			play_again = input(f"There are no more cards to choose from. Your final score is {my_score}. The computer's score is {comp_score}. You win! Care to play again? Y/N")
			play_again = play_again.upper()
			
			#RESTART GAME
			if play_again == "Y":
				restore_deck()
				#card_deck = copy.deepcopy(starting_deck)
				start_game()
			else:
				print("Game Over")
				return None
			
			return None
		elif comp_score > my_score:
			play_again = input(f"There are no more cards to choose from. Your final score is {my_score}. The computer's score is {comp_score}. You Lose. Care to play again? Y/N \n")
			play_again = play_again.upper()
			
			#RESTART GAME
			if play_again == "Y":
				restore_deck()
				#card_deck = copy.deepcopy(starting_deck)
				start_game()
				
			#GAME OVER SCREEN	
			else:
				print("Game Over")
				return None
				
		elif my_score == comp_score:
			play_again = input(f"There are no more cards in the deck. Your final score is {my_score}. The computer's score is {comp_score}. It's a draw! Care to play again? Y/N")
			play_again = play_again.upper()
			
			#RESTART GAME
			if play_again == "Y":
				restore_deck()
				#card_deck = copy.deepcopy(starting_deck)
				start_game()
				
			#GAME OVER SCREEN	
			else:
				print("Game Over")
				return None
	
	#if card_deck is not 0:	
	#	print('Good round! Would you like to continue?')
	#elif card_deck == None:
	#	break
			#print('Great game! Want to go again?')
			
			
	

start_game()
end_game()


