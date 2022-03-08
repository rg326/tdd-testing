# # #CARD PROBLEM - LINEAR SEARCH
##Time: O(N) Space: O(1)
# # # Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

# STEPS:

# Create a variable position with the value 0.
# Check whether the number at index position in card equals query.
# If it does, position is the answer and can be returned from the function
# If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
# If the number was not found, return -1.

# # def locate_card(cards, query):
# #     for pos in cards:
# #         if(pos == query):
# #             return pos
# #         elif(!pos == query):
# #             pos += 1
# #         else:
# #             return -1
# #     return  


def locate_cards(card, query):
	#Create a variable position with the value 0
	pos = 0
	
	#Keep track of the information:
	print('card:', cards)
	print('query', cards)
	
	#Set up a loop for repetition
	while pos < len(cards):
		
	print('position', pos)
	
	#Check whether the number at index position in card equals query.
	if card[pos] == query:
		
		#Answer found! Return and exit
		return pos
		
	pos += 1
	
	#Check if we have reached the end of the array:
	if pos == len(cards):
		
		#Number not found, return -1
		return -1
		
		
