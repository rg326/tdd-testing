# Unordered
# Immutable
# mapping of unique keys to values

# Python 3.6 and up, goes by insertion order

# Basic Operations
# - Creating an empty dictionary d = {}
# - Add an entry d["IV"] = 4
# - Add three items in the dictionary d = {"I":1, "II":2, "III": 3}
# - Delete an entry del d["IV"]
# Dictionaries are memory efficient starting in Python 3.6

'''
sal_info = {'Austin':91185,'Boston':90171}
sal_info['Boston'] = 95123
sal_info['Atlanta'] = 91234
print(sal_info)
len(sal_info)
del sal_info['Atlanta']
print(sal_info)
len(sal_info)
print(sal_info['Atlanta'])
sal_info.clear()
print(sal_info)
len()
'''

'''
sal_info = dict()
print(sal_info)

#Populate dictionary
sal_info = {'Austin':911985,'Dallas':89999,'San Jose':100989,'Atlanta':89286}
print(sal_info)

if('Dallas' in sal_info):
    print(sal_info['Dallas'])
else:
    print('not found')

for location in sal_info:
    print(sal_info[location]) # prints values

for location in sal_info:
    print(location) # prints keys
'''

# CHALLENGE

import csv
with open('file.file', mode='r') as infile:
    reader = csv.reader(ofile)

    mydict = {}

    for row in reader:
        key = row[0]
        mydict[key] = row[1]

sizeOfDi = len(mydict)
print(sizeOfDi)
# print('The dictionary is of size: ', str(sizeOfDi))

#code foor modifying a key - we will take the example of 281

mydict['205'] = 10
print(mydict)

# code for adding a key-value pair
mydict['999'] = 12
print(mydict)

infile.close()