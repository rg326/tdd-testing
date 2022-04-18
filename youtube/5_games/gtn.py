import random

def guess_the_num(num_range):
	print('Lets play: Guess The Number!')
	num_range = int(input('Please enter a number: '))
	
	random_num = random.randint(0, num_range)
	
	num_guess = 0
	
	while True: #good for tasks, actions that need to be repeated
		guess = int(input(f"Guess a number between 0 and {num_range}: "))
		num_guess += 1
		if guess == random_num:
			print(f"Congrats! The number is {random_num}")
		elif guess < random_num:
			print('The number is too low')
		else:
			print('The number is too high!')
		
