import random
import time

def rps():
	print('Choose your weapon! Rock, Paper, or Scissors!')
	choice = input()
	print(f"You chose: {choice}!")
	choices = ['Rock', 'Paper', 'Scissors']
	comp_choice = random.randint(0, 2)
	time.sleep(3)
	print(f"The computer chose: {choices[comp_choice]}!")
	
#	for i in choices:
#		indices = choices.index(i)
		
	if choice == 'Rock' or 'rock' and choice[comp_choice] == 0:
		time.sleep(2)
		print('It\'s a draw! Try again!')
	elif choice == 'Rock' or 'rock' and choice[comp_choice] == 1:
		time.sleep(2)
		print('Paper beats rock! You lose!')
	elif choice == 'Rock' or 'rock' and choice[comp_choice] == 2:
		time.sleep(2)
		print('Rock beats scissors! You win!')
	elif choice == 'Paper' or 'paper' and choice[comp_choice] == 0:
		time.sleep(2)
		print('Paper beats rock! You win!')
	elif choice == 'Paper' or 'paper' and choice[comp_choice] == 1:
		time.sleep(2)
		print('It\'s a draw! Try again!')
	elif choice == 'Paper' or 'paper' and choice[comp_choice] == 2:
		time.sleep(2)
		print('Scissors beats paper! You lose!')
	elif choice == 'Scissors' or 'scissors' and choice[comp_choice] == 0:
		time.sleep(2)
		print('Rock beats scissors! You lose!')
	elif choice == 'Scissors' or 'scissors' and choice[comp_choice] == 1:
		time.sleep(2)
		print('Scissors beats paper! You win!')
	elif choice == 'Scissors' or 'scissors' and choice[comp_choice] == 2:
		time.sleep(2)
		print('It\'s a draw! Try again!')
	
	
	play_again = input('Great game! Would you like to play again? (y/n)')
	
	if play_again == 'y':
		rps()
	elif play_again == 'n':
		return None
	
	
	
rps()
