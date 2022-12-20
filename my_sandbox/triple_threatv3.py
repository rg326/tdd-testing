#NOTES




# =========

# Import modules
import random
import copy
import time

#Variables

starting_deck = {}

starting_deck = create_deck()

#COPYING STARTING DECK BY VALUE TO EMPTY CARD DECK
#card_deck = {}
card_deck = copy.deepcopy(starting_deck)

#Getting the keys of the deck as an array for each hand played
hand = card_deck.keys()

#--------------------------

def start_game():
	global starting_deck
	global create_deck
	global card_deck




#--------------------------
def play_turn():
	global hand
	global my_score
	global comp_score
	global my_hand
	global comp_hand
	global starting_deck
	global card_deck