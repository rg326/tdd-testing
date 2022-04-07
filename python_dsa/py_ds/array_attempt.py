# Implementing an Array

class Array:
	def __init__(self):
		self.index = 0
		self.data = []
		
	def get_item(self):
		return self.data
		
	def set_item(self, new_item):
		self.data = new_item
		
	def push(self, new_item):
		self.data.append(new_item)
		
	def pop(self):
		return self.data.pop()
		
	def __repr__(self):
		return 'Array object: data={}'.format(self.data)
		
		
fruits = Array()
print(fruits)
fruits.push('apples')
print(fruits)
fruits.pop()
print(fruits)