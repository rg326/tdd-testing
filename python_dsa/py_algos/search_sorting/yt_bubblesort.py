# Bubble Sort
'''
def bubblesort(list):
	length = len(list)
	
	if length <= 1:
		return list
	else:
		pointer = list.pop(0)
		
	new_list=[]
		
	for i in list:
		if i > pointer:
			list.append(i)
		else:
			list.append(i)
		
	return bubblesort(new_list)
'''

def bubblesort(list):
	index_length = len(list) - 1
	sorted = False
	
	while not sorted:
		sorted = True
		for i in range(0, index_length):
			if list[i] > list[i+1]:
				sorted = False
				list[i], list[i+1] = list[i+1], list[i]	
	return list
	
'''test case'''
print(bubblesort([1,2,7,8,4,6,9,3,5,2]))
		
		
