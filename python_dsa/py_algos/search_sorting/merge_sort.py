#Similar to binary search, but each comparison operation cuts down the range to half the values
# Uses comparison Operations
# O(n log n)

def merge_sort(list):
	if len(list) > 1:
		midpoint = len(list)//2 #floor divider for list's halfway point
		
		left_list = list[:midpoint] #only sort lower bound
		right_list = list[midpoint:] #only sort higher bound
		
		merge_sort(left_list)
		merge_sort(right_list)
		
		i = j = k = 0 #initiate indices for all three lists to zero
		
		while i < len(left_list) and j < len(right_list):
			if left_list[i] < right_list[j]:
				list[k] = left_list[i]
				i += 1
				
		else:
			list[k] = right_list[j]
			j += 1
			k += 1
		
		while i < len(left_list):
			list[k] = left_list[i]
			i += 1
			k += 1
			
		while j < len(right_list):
			list[k] = right_list[j]
			j += 1
			k += 1
			
def print_sortedlist(list):
	for i in range(len(list)):
		print(list[i], end='')
		print()
		
		
arr = [6,3,9,6,7,22,87,45,34]
print_sortedlist(arr)
merge_sort(arr)
print_sortedlist(arr)
	
