def weather_condition(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"

user_input = int(input("Enter some input:"))

print(type(user_input), user_input)

 #Final Notes
 # In this section you learned that:
 # A python program can get user input via the input function
 # The input function halts the eecution of the program and gets text input from the user

 name = input("Enter your name: ")

 # The input function converts any input to a string, but you can convert it back to int or float:

 experience_months = input("Enter your experience in months: ")
 experience_years = int(experience_months) /12

 # You can also format strings with:

 name = "Sim"
 experience_years = 1.5
 print("Hi {}, you have {} years of experience").format(name, experience_years))
 # Output: Hi Sim, you have 1.5 years of experience. 