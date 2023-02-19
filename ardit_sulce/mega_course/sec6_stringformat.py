# String Formatting

user_input = input("Enter your name: ")
message = "Hello %s!" % user_input #Python 2.3
message = f"Hello {user_input}" #Python 3^
print(message)

#Multiple strings/variable inputs for Python 2.3
message = "Hello %s" % (name, surname)