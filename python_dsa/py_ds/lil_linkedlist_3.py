# Implementation Linked List - LinkedIn Learning

class DLLNode: #Doubly Linked List (DLL)
	
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None
		
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
		
	def get_previous(self):
		'''Return the self.previous attribute'''
		return self.previous
	
	def set_previous(self, new_previous):
		'''Replace the existing value of the self.previous attribute with new_previous parameter.'''
		self.previous = new_previous

'''		
node = DLLNode('apple')
dataget = node.get_data()
print(dataget)

setdata = node.set_data('7')
print(setdata)

node2 = DLLNode('carrot') #each is its own list
setnext = node.set_next(node2)
print(setnext)
getnext = node.get_next()
print(getnext)
'''
# Double linked list needs both a get_next and a get_previous method

node1 = DLLNode(1)
node2 = DLLNode(2)
getprev = node1.get_previous()
print(getprev)
setprevious = node1.set_previous(node2) 
print(setprevious)
