# String Formatting

user_input = input("Enter your name: ")
message = "Hello %s!" % user_input #Python 2.3
message = f"Hello {user_input}" #Python 3^
print(message)

#Multiple strings/variable inputs for Python 2.3
message = "Hello %s" % (name, surname)

#Python 3
when = "today"
message = f"Hello {name}{surname}. What's up {when}?"
print(message)
# //Hello Name, Surname. What's up today?

# Exercise Formatting Strings
def greet(name):
    return f"Hi {name}"

# Formatting and Uppercase
def upper(name):
    return f"Hi {name.title()"