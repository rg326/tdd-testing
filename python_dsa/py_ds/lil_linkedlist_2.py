# Implementation Linked List - LinkedIn Learning

class SLLNode: 
	
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
		
node = SLLNode('apple')
dataget = node.get_data()
print(dataget)

setdata = node.set_data('7')
print(setdata)

node2 = SLLNode('carrot') #each is its own list
setnext = node.set_next(node2)
print(setnext)
getnext = node.get_next()
print(getnext)
