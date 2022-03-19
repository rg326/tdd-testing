def quicksort(list):
	length = len(list)
	'''base case'''
	if length <= 1:
		return list
	else:
		pivot = list.pop()
	
	items_low = []
	items_high = []
	
	for i in list:
		if i < pivot:
			items_low.append(i)
		else:
			items_high.append(i)
			
	return quicksort(items_low) + [pivot] + quicksort(items_high)
	
'''test case'''	
print(quicksort([1,2,3,6,5,9,4,6,8,0,2]))
