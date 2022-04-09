# Binary Tree and Breadth First Search (Algorithm)

# Tree = 'gcbaedfihjk'

# Class BTree = Tree Node construction

class BTree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
	def insert(self, data):
		if self.data is None:
			self.data = data
		else:
			if data < self.data:
				if self.left is None:
					self.left = TreeNode(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = TreeNode(data)
				else:
					self.right.insert(data)
					
root = BTree('g')
root.insert('c')
root.insert('b')
root.insert('a')
root.insert('e')
root.insert('d')
root.insert('f')
root.insert('i')
root.insert('h')
root.insert('k')