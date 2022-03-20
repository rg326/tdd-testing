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

	
	
'''test case'''
print(bubblesort([1,2,8,4,6,9,3,2]))
		
		
