#### 1 Python Dictionary Basic Operations - Linkedin Learning

# Change an Entry - d['II'] = 'two'
# Delete an Entry - del d['IV']
# Remove all items - d.clear()


sal_info = {'Austin': 911985, 'Dallas': 89999, 'San Jose': 100989, 'Atlanta': 92340, 'Portland': 101367}
'''
if 'Seattle' not in sal_info:
	sal_info['Seattle'] = 110340
else:
	print('Key exists')
	
print(sal_info)
'''

#### 2 Python Dictionary Basic Methods

# Access a value from a dictionary - d.get(key, default msg)
'''
print(sal_info.get('Dallas', 'not found'))
>>> 8999
print(sal_info.get('NYC', 'not found'))
>>> not found
'''

# Find the max value in the dictionary d.max()
# Find the min value in the dictionary d.min()
# Return the value associated with the key(removed the key-value pair from the dictionary) - d.pop(key, default)

# Return a sorted list - d.sorted()
# Make a shallow copy of the dictionary - d.copy()

'''
print(sal_info.keys())
print(sal_info.values())

print('Key-Value Pair')
for k,v in sal_info.items():
	print('The key is: ', k, 'the value is: ', v)
	
print('The city with the highest salary', max(sal_info, key=sal_info.get))
print('The city with the lowest salary', min(sal_info, key=sal_info.get))

#print(sal_info)

print('Value of key', str(sal_info.pop('Dallas', 'not found')))
#print(sal_info)

print(sal_info.popitem())
#print(sal_info)

#Prints dictionaries with keys sorted
print(sal_info)
print(sorted(sal_info.keys()))
print(sorted(sal_info.values()))
'''

#### 3 Using Lists within a Dictionary
'''
eng_di = {}

#Adding lists as a value
eng_di['solitude'] = ['lone', 'lonely', 'alone', 'unaccompanied', 'without society']
eng_di['hope'] = ['aspiration', 'desire', 'wish', 'expectation', 'ambition']
print(eng_di)

#Creating a dictionary with an empty list
eng_di.clear()
eng_di = {'solitude':[]}
eng_words = ['lone', 'lonely', 'alone', 'unaccompanied', 'without society']
eng_di['solitude'].append(eng_words[0])
print(eng_di)

eng_di['solitude'] = eng_words
print(eng_di)

if (eng_di.get('solitude')): #If key 'solitude' exists
	for list_item in eng_di['solitude']: # for each item in 'solitude'
		print(list_item) # print each item
else:
	print('word not in dictionary') #Print if key doesn't exist'
'''

# Christmas Tree Challenge
import csv

#import excel spreadsheet
with open('TreeOrderSubset.csv', mode='r') as infile:
	reader = csv.reader(infile)
	treeOrders = {} # dict has key as subdivision id, val as the o
	for row in reader:
		key = row[0]
		
#remove this before recording
		if (key not in tree):
			treeNum = row[1]
			treeOrders[key] = treeNum
		else:
			treeNum = row[1]
			prev_count = treeOrders[key]
			treeOrders[key] = int(prev_count) + int(treeNum)
			
print(treeOrders.items())
	
infile.close()
	
