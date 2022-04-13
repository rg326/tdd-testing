# BubbleSort Practice

def bubblesort(list):
	length = len(list)-1
	
	for i in range(0, length):
		for j in range(length):
			if(list[j] > list[j+1]):
				temp_storage = list[j]
				list[j] = list[j+1]
				list[j+1] = temp_storage
	return list
		
		
print(bubblesort([7,3,6,3,4,6,5,6]))

def bubblesort2(list):
		pass