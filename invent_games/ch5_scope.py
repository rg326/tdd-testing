import random

def bacon():
	spam = 99 #Creates a local variable named spam
	print(spam) #Prints 99
	
spam = 42 #Creates a global variable named spam
print(spam) #Prints 42
bacon() #Calls the bacon function and prints 99
print(spam) #Prints 42

str(5)
print(random.randint(1, 20))
print(len('Hello'))
