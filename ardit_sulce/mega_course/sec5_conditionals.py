#Intro to Conditionals

def mean(val):
    if type(val) == dict:
        the mean = sum(val.values() / len(val))
    else:    
        the_mean = sum(myList) / len(myList)
        return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

print(mean(student_grades))
j
#Allows to control for different avenues or branches of choices

# Elif conditionals
x = 3
y = 1
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")