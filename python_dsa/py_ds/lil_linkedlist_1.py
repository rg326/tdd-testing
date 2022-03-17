#Linked List - LinkedIn Learning

##### Abstract Data Types (ADTs) 

# ADTs - A theoretical concept to specify what kind of data a data structure can hold and what operations are allowed to that data
# No code
# Interaction, not implementation
# Language agnostic
# Data Structures (DSs) - Concrete implementations of ADTs that organize and retrieve data stored in memory

# Advantages of ADTs:
# Abstraction - All the user needs to know are the allowable data types and allowable operations
# No understanding of the implementation is required
# Consistency - The implementation can change as long as the interface to the data structure stays the same
	# The user doesn't have to alter their code
# One ADT Operation = One function/method in class in DS
# Often more than one implementation of an ADT
# Understanding the difference between abstract data types and data structures will help you communicate more effectively about both

#### The Built-In List Data Type in Python
# ex: [1, 'apple', 57, 84.3, 'berry', False, [1,2]]
# A mutable, ordered collection of items that do not have to be of the same type; implemented in C using a dynamic array
# The python language is written in C
# Dynamic arrays: 
	# use a contiguous chunk of memory
	# allow us to index directly to a slot in memory
	# reserve more continguous memory than is actually needed
# We can append to the end of dynamic arrays in constant time
# Linked List - A mutable, ordered collection of items that do not have to be the same data type, but they're very different than built-in lists.

# The Linked List ADT - Nodes:
# Linked List don't store their data in continugous chunks of memory, but rather in a series of nodes. Each node contains the data being stored, as well as a pointer, which indicates the location in memory that holds the next node.
# The pointers describe the order in which the nodes should be accessed.
# This creates a structure that resembles the inherently ordered nature of a Python built-in list.
# There are two kinds of pointers: previous and next. 
# Singly linked lists only make use of the next pointer. They only allow you to move in forward in memory.
# Doubly linked lists make use of both both the previous and next pointers. They allow you to move forward and backward in memory.

#### Operations:
	
# Adding Nodes - at head or tail, before/after a given key
# Removing Nodes - at head or tail, before/after a given key
# Other Operations:
	# Is the linked list empty?
	# How many nodes are in it?
	# Find a node's index given its key
# Linked lists are sequential access data structures
# When is a Linked List suitable:
	# Insert items 'in-between' other items
	# Collection size is unknown
# Linked lists are recursive DSs:
	# they're either empty or consists of/is a node that contains data and a pointer to a linked list
