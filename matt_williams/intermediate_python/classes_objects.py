our_dog = {
	'name': 'Bruno',
	'color': 'brown'
}

#use bracket syntax for dictionary
print(our_dog['name'])

def describe(dog):
	return f"{dog['name']} is {dog['color']}."
	
doggo = describe(our_dog)
print(doggo)
	
#the class	
class Dog:
	def __init__(self, name, color):
		self.name = name
		self.color = color
		self.energy = 1
		
		def describe(self):
			return f"{self.name} is {self.color}."
			
		def exercise(self):
			print(f"You take {self.name} for a walk.")
			self.energy -= 1
			
		def feed(self):
			print(f"{self.name} eats the food.")
			self.energy += 1	
		
	
#use object syntax for class			
our_dog = Dog('Bruno', 'brown')

#use bracket syntax 
print(our_dog.name)

#def describe(dog):
#	return f"{dog.name} is {dog.color}."
	
doggo = describe(our_dog)
print(doggo)

other_dog = Dog('Achilles', 'blue')

#def call_dog(dog):
#	print(describe(dog))
	
#call_dog(other_dog)
