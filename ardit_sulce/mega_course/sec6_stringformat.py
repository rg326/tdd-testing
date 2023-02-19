# String Formatting

user_input = input("Enter your name: ")
message = "Hello %s!" % user_input #Python 2.3
message = f"Hello {user_input}" #Python 3^
print(message)