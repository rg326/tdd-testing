# Understanding Comprehension - Linked Learning


#### 4 Types of Python Dict Comprehension
# List comprehension
# Dictionary comprehension
# Set comprehension
# Generator eomprehension - are fundamental structures from which list, set, and dictionary structures are created.

# A Python Comprehension has 3 parts:
	# Output: Dictionary key-value pair
	# Input: Loop iteration needed for computation
	# Conditional: Optional - needed only if computation required
	
#sal_info = {'Austin': 911985, 'Dallas': 89999, 'San Jose': 100989, 'Atlanta': 92340, 'Portland': 101367}

'''
sal_data_keys = ['Austin','Portland', 'Dallas', 'Atlanta']
sal_data_values = [91185, 110123, 89123, 112000]

sal_info = {}
print('#### Creating a dictionary without comprehension')
for key, value in zip(sal_data_keys, sal_data_values):
	sal_info[key] = value
print(sal_info)
sal_info.clear()

# Using Dictionary Comprehension to populate the dictionary
print('#### Creating a dictionary using comprehension')

sal_info = {sal_data_keys[index]:sal_data_values[index] for index in range (0, len(sal_data_keys))}
print(sal_info)
'''

#### Iteration and Computation
'''
sal_100k = {}
for k in sal_info:
	if sal_info[k] > 100000:
		sal_100k[k] = sal_info[k]
		
print(sal_100k)
sal_100k.clear()

#filtering through the dictionary using comprehension
sal_100k = {k : v for k,v in sal_info.items() if v > 100000}
print(sal_100k)
'''	

# Challenge

reader = csv.reader(infile)
treeOrders = {}
for row in reader: 
	key = row[0]
	
	if(key not in treeOrders):
		treeNum = row[1]
		treeOrders[key] = int(treeNum)
		
	else:
		treeNum = row[1]
		prev_count = treeOrders[key]
		treeOrders[key] = int (prev_count) + int (treeNum)
		
infile.close()
print('length of dictionary', len(treeOrders))
# Create a new dict treeOrders10 with subdivisions that have more than 10 trees
# Use dict comprehension
treeOrders10 - {k:v for k,v in treeOrders.items() if v > 10}

print(treeOrders10)
print('length of dictionary',lens(treeOrders10))
