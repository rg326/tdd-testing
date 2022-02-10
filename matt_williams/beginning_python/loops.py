words = ['Hello','Python']

#print(word)

#word = 'Python'

print(words)

for word in words:
	print('...')
	print(word)
	print('end')
	
##VS

for word in words:
	print('...')
	print(word)
print('end')

##Ending indentation only loops '...' and word variable

##Range and looping in a loop
##Instead of
#for word in words:
#	print(word)
#	print(word)
#	x100
#Do:
#for word in words:
#	for repeat in range(100):
#		print(word)

##Enumerate gives the index alongside the item
for word in enumerate(words):
	print(word)
	
for i, word in enumerate(words):
	print('Item', i, 'is', word)
	
##dummy variables
for i, word in enumerate(words):
	my_num = 42
	print('Item', i, 'is', word)
	print(my_num)
