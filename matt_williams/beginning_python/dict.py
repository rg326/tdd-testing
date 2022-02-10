sounds = {
	'cat':'meow',
	'dog': ['woof', 'bark'],
	'penguin': 'meep',
	'fox': 'screech',
	'bird': 'tweet',
	'duck': 'quack',
	'sheep': 'baaah',
	'fish': 'glub'
}

cat_sound = sounds['cat']
print(cat_sound)

sounds['tiger'] = 'grrr'
tiger_sound = sounds['tiger']
print(tiger_sound)

##Rename key - 2 step process
#sounds['new key'] = sounds['old key']
#del sound['old key']

for thing in sounds:
	print(thing)

for thing in sounds:
	print(sounds[thing])
	
##alt

for animal in sounds.keys():
	print(animal)

for animal in sounds.values():
	print(animal)
	
##Works similar to enumerate method:
for thing in sounds.items():
	print(thing)
	
for animal, sound in sounds.items():
	if animal == 'dog':
		print(animal, 'goes', sound[0], 'and', sound[1])
	else:
		print(animal, 'goes', sound)
		
##ALT of above
for animal, sound in sounds.items():
	if isinstance(sound, list): 
		#list as in the actual data type, which sounds['dog'] is
		print(animal, 'goes', sound[0], 'and', sound[1])
	else:
		print(animal, 'goes', sound)
