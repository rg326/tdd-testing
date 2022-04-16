# Treehouse - Recoursive Binary Search

# Does not return None, but False if it doesn't exist

def recursive_binary_search(list, t):
	#base case:
		if len(list) == 0:
			return False
		else:
			midpoint = len(list)//2
			
		if list[midpoint] == t:
			return True
		else:
			if list[midpoint] < t:
				return recursive_binary_search(list[midpoint+1:], t)
			else:
				return recursive_binary_search(list[:midpoint], t)
				
def verify(result):
	print('Target found: ', result)
	
numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(numbers, 12)
verify(result)
result = recursive_binary_search(numbers, 6)
verify(result)
result = recursive_binary_search(numbers, 5)
verify(result)
	
