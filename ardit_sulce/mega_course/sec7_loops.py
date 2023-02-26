monday_temp = [9.1, 8.8, 7.6]

print(round(monday_temp[0])) #x3

#For loops automatically reiterate over commands
for temp in monday_temp:
    print(round(temp)) 

for letter in "hello":
    print(letter.title())

# Exercise - Loop Over Colors
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    print(color)

# Exercise - Loop Over Big Colors

for color in colors:
    if color > 50:
        print(color)


# Exercise - Loop Over Integer Colors
colors = [11, 34.1, 98.2, 43, 45.1, 54 ,54]

for color in colors:
    if color % 1 == 0:
        print(color)

# Alt
for color in colors:
    if isinstance(color, int):
        print(color)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int) and color > 50:
        print(color) 

# For Loop Over a Function
def cels_to_kel:
    return cels + 273.15

for temp in [9.1, 8.8, -270.15]:
    print(cels_to_kel(temp))
