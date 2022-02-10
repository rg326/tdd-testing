my_num = 128

if my_num > 100:
	print(my_num, 'is large')

#	> greater than
#	< less than
#	>= greater than or equal
#	<= less than or equal
#	== equal
#	!= not equal

if my_num > 100:
	print(my_num, 'is large')
else:
	print(my_num, 'is small')


if my_num > 100:
	print(my_num, 'is large')
elif my_num == 100:
	print(my_num, 'is 100')
else:
	print(my_num, 'is small')

for num in range(100):
	if num % 2 == 0:
		print(num, 'fizz')
	elif num % 3 == 0:
		print(num, 'buzz')
	else:
		print(num, 'fizzbuzz')
