# Binary Search Algorithm O(nlogn) - List Must Be Sorted

def binary_search(list, t):
	low = 0
	mid = len(list)//2 #floor divider
	high = len(list)-1
	
	while low <= high:
		mid_val = list[mid] #the val at mid pos in list
		if mid_val == t:
			return mid
		elif t < mid_val:
			high = mid - 1 # change list to start at mid (1 pos below)
		else:
			low = mid + 1 # change list	to start 1 pos above mid
			
	return None


list_test = [1,2,3,4,5,6,7,8,9,10]

print(binary_search(list_test, 4))
print(binary_search(list_test, 11))
