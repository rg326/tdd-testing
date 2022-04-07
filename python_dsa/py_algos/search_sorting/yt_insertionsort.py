# Insertion Sort - Youtube

def insertion_sort(list):
	index_length = range(1, len(list))
	
	for i in index_length:
		val_to_sort = list[i]
		
		while list[i-1] > val_to_sort and i > 0:
			list[i], list[i-1] = list[i - 1], list[i]
			i -= 1
			
	return list
