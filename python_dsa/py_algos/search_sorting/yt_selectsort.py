# Selection Sort - Youtube

def selection_sort(list):
	index_length = range(0, len(list)-1)
	
	for i in index_length:
		min_val = i
		
		for j in range(i+1, len(list)):
			if list[j] < list[min_val]:
				min_val = j
			
		if min_val != i:
			list[min_val], list[i] = list[i], list[min_val]
			
	return list
		
print(selection_sort([3,8,4,8,5,6,4,8,9,7,4,1,2,4]))
		
