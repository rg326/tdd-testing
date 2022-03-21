# Creating the Singly Linked List Class and Its Methods

'''Node Class'''

class SLLNode: # Single Linked List (SLL) 
	
	def __init__(self, data):
		self.data = data
		self.next = None
		
	def __repr__(self):
		return 'SLLNode object: data={}'.format(self.data)
		
	def get_data(self):
		'''Return the self.data attribute'''
		return self.data
		
	def set_data(self, new_data):
		'''Replace the existing value of the self.data attribute with new_data parameter'''
		self.data = new_data
		
	def get_next(self):
		'''Return the self.next attribute'''
		return self.next
		
	def set_next(self, new_next):
		'''Replace the existing value of the self.next attribute with new_next parameter.'''
		self.next = new_next
		
'''Singly Linked List Class'''

class SLL:
	
	def __init__(self):
		self.head = None
		
	def __repr__(self):
		return 'SLL object: head={}'.format(self.head)
		
	def is_empty(self):
		'''Returns True/False depending on if Linked List is empty'''
		if self.head == None:
			return True
		else:
			return False
		#can also say return self.head is None (more pythonic), or self.head == None
	
	def add_front(self, new_data):
		'''Add a Node whose data is the new_data argument to the front of the linked list'''
		temp = SLLNode(new_data)
		temp.set_next(self.head)
		self.head = temp
		
	def size(self):
		'''Traverse the linked list and returns an int value representing the number of nodes in the list. Time Complexity: O(n) bc every node in the linked list must be visited in order to calculate the total size'''
		size = 0
		if self.head is None:
			return 0
		
		current = self.head
		
		while current is not None: #While there are still nodes present
			size += 1
			current = current.get_next()
			
		return size
		
	def search(self, data):
		'''Traverses the linked list and returns True if the data searched for is present in one of the Nodes. Otherwise, it returns False.
		
		Time Complexity is O(n) bc every node must be visited in the worst case scenario.'''
		if self.head == None:
			return 'Linked list is empty. No nodes to search.'
		
		current = self.head
		while current is not None:
			# The Node's data matches what we're looking for
			if current.get_data() == data:
				return True
			# The Node's data doesn't match
			else:
				current = current.get_next()
				
		return False
				
		
	def remove(self, data):
		'''Removes the first occurence of a node that contains the data argument as its self.data variable. Returns nothing.
		
		Time complexity: O(n) bc in the worst case, the node we want to remove is the last so we'd have to visit every node.'''
		if self.head == None:
			return 'Linked list is empty. No nodes to remove.'
		
		current = self.head
		previous = None
		found = False
		while not found:
			if current.get_data() == data:
				found = True
			else:
				if current.get_next() == None:
					return 'A node with that data value is not present.'
				else:
					previous = current
					current = current.get_next()
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())
			
		
'''Test cases'''
'''
sll = SLL()
print(sll.is_empty())
node = SLLNode(5)
sll.head = node
print(sll.is_empty())
'''
'''
sll = SLL()
sll.head
sll.add_front('berry')
print(sll.head)
'''
'''
sll = SLL()
print(sll.size)
sll.add_front(1)
sll.add_front(2)
sll.add_front(3)
print(sll.size)
'''
'''
sll = SLL()
print(sll.search(3))
sll.add_front(1)
sll.add_front(2)
sll.add_front(3)
print(sll.search('bird'))
print(sll.search(2))
'''

'''
sll = SLL()
print(sll.remove(15))
sll.add_front(27)
print(sll.remove(15))
print(sll.remove(27))
print(sll.head)
sll.add_front('apple')
sll.add_front('berry')
sll.add_front('cherry')
sll.remove('berry')
print(sll.head)
print(sll.head.next)
'''

