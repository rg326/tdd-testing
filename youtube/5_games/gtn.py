import random

def guess_the_num(x):
	print('Lets play: Guess The Number!')
	
	random_num = random.randint(0, x)
	
	num_guess = 0
	
	while True: #good for tasks, actions that need to be repeated
