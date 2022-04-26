import random

words = (
	"awake",
	"blush",
	"focal",
	"evade",
	"serve",
	"model",
	"karma",
	"grade",
	"quiet"
	)

class Wordle:
	def __init__(self):
		self.word = random.choice(words)
		self.num = 0
		self.guess_dict = {
			0: [""]*5,
			0: [""]*5,
			0: [""]*5,
			0: [""]*5,
			0: [""]*5
		}
		
		def draw_board(self):
			for guess in self.guess_dict.values():
				print(" | ").join(guess))
				print("==========")
				
		def get_user_input(self):
			user_guess = input("Enter a 5 letter word: ")
			while len(user_guess) is not 5:
				user_guess = input("Not valid. Please enter a 5 letter word.")
				
			user_guess = user_guess.lower()
			for i, char in enumerate(user_guess): #gives both index+val
			
		def play(self): #game loop
			while True:
				self.draw_board()
				user_guess = self.get_user_input
				if user is self.word:
					self.draw_board()
					print(f"You won! The word was {self.word}")
				
				if self.num_guesses > 5:
					self.draw_board()
					print(f"You lost! The word was {self.word}")	
		
