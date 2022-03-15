# Dict vs Other Data Structures - LinkedIn Learning

#### Dict vs Lists
sal_info_keys = ['Austin', 'Portland', 'Dallas']
sal_info_values = [91185, 110123, 89123]

# Printing original keys-value list
print('Original key lists is : ' + str(sal_info_keys))
print('Original key lists is : ' + str(sal_info_values))
# to convert lists to dictionary

sal_info = {}

print('#### Method 1 using for in ')
index = 0
for key in sal_info_keys:
	value = sal_info_values[index]
	sal_info[key] = value
	index += 1
	
# Printing resultant dictionary
print('Resultant dictionary is : ' +str(sal_info))

#### Dict vs sets and tuples
# Tuple is a collection that is ordered, unchangeable and indexed/sorted. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection that is unordered, changeable, and indexed. No duplicate keys, but values can be duplicated.
# Dictionaries, lists, and tuples give better control in accessing the data.
# Dictionaries and sets have fast access times compared to lists and tuples


#tuples
'''
Cities = {'Austin': 81111, 'Dallas': 91345}
print(citi_info['Dallas'])
print(citi_info)
'''

# sets
'''
city_names_set = {'Austin', 'Portland', 'Dallas', 'Austin'}
print(city_names_set)
for set_value in city_names_set:
	print(set_value)
'''

#### Implementations of Dictionaries as Hash Tables
# A hash table's goal is to keep the data evenly distributed across the table
# At least one-third empty
# Hashable objects that compare equal must have the same hash value consistently
# Dictionary keys must be immutable - for example, str, bytes, numeric
# Cells in a hash table are called buckets
# Python has a built-in hash function
# Collisions happen when two unique keys have the same hash code
# Keys must be immutable
# Significant memory overhead (spare arrays in Python 3.6 solves this issue)
# Key search is very fast.
# Key ordering depends on insertion order.
# Adding items to the dictionary may change the order of the existing keys.





