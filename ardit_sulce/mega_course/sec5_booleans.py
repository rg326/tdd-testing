# AND and OR operators

x = 1
if x == 1:
    print("Yes")
else:
    print("No")

# You can check if two conditions are met at the same time using an and operator
x = 1
y = 1

if x == 1 and y == 1:
    print("Yes")
else:
    print("No")

# This will return "Yes", since x == 1 and y == 1 are both True

# You can also check if one or two conditions are met using an or operator

x = 1
y = 1

if x == 1 or y == 2:
    print("Yes")
else:
    print("No")

# That will return Yes since at least one of the conditions is True. In this case, x == 1 is True.

#For github: push 1 Feb 9, 2023
#For github: push 2 Feb 9, 2023

# Ex Warm or Cold:

def worc(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"

# Ex Password Controller:

def pass_controller(str):
    if len(str) >= 8:
        return True
    else:
        return False

# Ex Hot, Warm, Cold

def temp_change(temp):
    if temp > 25:
        return "Hot"
    elif temp >= 15 and temp <= 25:
        return "Warm"
    elif temp < 15:
        return "Cold"