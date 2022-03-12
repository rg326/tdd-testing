#Treehouse - Binary Search

# Unlike linear search, the list MUST be sorted in order to implement binary search
#

def binary_search(list, t):
	first = 0
	last = len(list) - 1 # Gets the last pos from the list
	
	while first <= last: #less than or equal in order to include last
		midpoint = (first + last)//2 #floor divider rounds to whole num
		
		if list[midpoint] == t:
			return midpoint
		elif list[midpoint] < t:
			first = midpoint + 1
		else:
			less = midpoint - 1
			
	return None # return None as default
	
def verify(index):
	if index is not None:
		print('Target found at index:', index)
	else:
		print('Target not found')
	
#Test Cases
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)
result = binary_search(numbers, 6)
verify(result)
result = binary_search(numbers, 5)
verify(result)

'''
Note: fix 'Target not found error'
'''



