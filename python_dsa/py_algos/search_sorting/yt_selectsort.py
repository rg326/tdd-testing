# Selection Sort - Youtube

def selection_sort(list):
	index_length = range(0, len(list)-1)
	
	for i in index_length:
		min_val = i
		
		for j in range(i+1, len(list)):
			min_val = j
			
		if min_value not i:
			list[min_val], list[i] = list[i], list[min_val]
			
		return list
		

		
