# Create an algo to find the h-index of a researcher's publications

def h_index(list):
	h = len(list)
	list.sort(reverse = True)
	count = 0
	
	for n in list:
		if n >= h:
			count += 1
			
	return count

print(h_index([2,7,4,8]))

print(h_index([1,7,6,5,6,]))


#def addition(num_a, num_b):
#	print(num_a + num_b)
	
# addition(3, 5)
