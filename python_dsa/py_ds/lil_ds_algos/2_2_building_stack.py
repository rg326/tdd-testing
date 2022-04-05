#### Write a Stack Class in Python

# Using a class to represent a stack

# Learning push and pop

# Using a list allows others to use insert, remove, etc. (ruins the point of defining a stack as it no longer functions the way it should)

## Stack is LIFO - Last In, First Out

# Add item to top of stack: append()
# Retrieve item from top of stack: pop()
# Both happen from the right(end of stack)

class Stack:
	def __init__(self):
		self.items = []


	def isEmpty(self):
		# return len(self.items) == 0
		return not self.items
		
	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		self.items.pop()
		
	def peek(self):
		return self.items[-1]
		
	def size(self):
		return len(self.items)
		
	def __str__(self):
		return str(self.items)
		
if __name__ == '__main__':
	s = Stack()
	print(s)
	print(s.isEmpty())
	s.push(3)
	print(s)
	s.push(7)
	s.push(5)
	print(s)
	print(s.pop())
	print(s)
	print(s.peek())	
	print(s.size())
