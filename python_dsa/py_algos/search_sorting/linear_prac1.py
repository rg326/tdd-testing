# Linear Search Practice

def linear_search(list, target):
	for i in range(len(list)):
		if list[i] == target:
			return True
	return False
	
print(linear_search([3,4,7,5], 4))
			
