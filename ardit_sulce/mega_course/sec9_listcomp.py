#Intro to List Comprehensions
temps = [221, 234, 340, 230]

# Not using decimals/floats saves space on servers

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

# A neater way to do this: list comprehension
new_temps = [temp / 10 for temp in temps]

print(new_temps)
