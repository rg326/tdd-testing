#auto open and close 'content manager'' - with statement
with open('data.txt') as fil:
	for line in fil:
		line = line.strip() #removes new line space
		line = int(line)
		print(line * 2)
		print(line, end='')
