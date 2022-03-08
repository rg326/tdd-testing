class Dog:
	def __init__(self, name, color):
		self.name = name
		self.color = color
		self.energy = 1
		
		def describe(self):
			return f"{self.name} is {self.color}."
			
		def exercise(self):
			if self.energy >= 1:
				print(f"You take {self.name} for a walk.")
				self.energy -= 1
			else:
				raise RuntimeError(f"{self.name} is tired. It doesn't want to walk.")
			
		def feed(self):
			print(f"{self.name} eats the food.")
			self.energy += 1
			
other_dog = Dog('Bruno', 'brown')

other_dog.exercise()

try:
	other_dog.exercise()
except RuntimeError as e: #as e is optional, allows variable to be used 
	print(f"Something went wrong while trying to exerise the dog: {e}.")
	other_dog.feed()
	other_dog.exerise()
	
#from dog.py/dog import Dog as dog
	
