a = 3

while a > 0:
    print(1)
    print(2)
    a += 1

# Will loop indefinitely unless incremented
# ex: a += 1

# while loop with user input
username = " "

while username != "pypy":
    username = input("Enter Username: ")

#Break and Continue
while True:
    username = input("Enter username: ")
    if username == "pypy":
        break
    else:
        continue

# Date and Time
#We also have while-loops. The code under a while-loop will run as long as the while-loop condition is true:

    while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
        print("It's not yet 19:30:20 of 2090.8.20")

#The loop above will print out the string inside print() over and over again until the 20th of August, 2090.
