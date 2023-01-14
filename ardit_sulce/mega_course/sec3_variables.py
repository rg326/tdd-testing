# 変数
# better to have spaces around the operator for better readability

spent = 3

donated = 4

total_amount = spent + donated

print(total_amount)

items = 10
price = 2

total_price = items * price

print(total_price)

# TIP - print multiple variables with a comma
print(total_price, items, price)

# exit() <- takes you out of the python interactive shell


#=====

x = 10
y = '10'
z = 10.1

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

#====

student_grades = [9.1, 8.8, 7.5]
student_grades = [9, "Hello", [1, 2, 3, 4]]


print(student_grades * 2)

student_grades = list(range(0, 11))

print(student_grades)
#//will list range between 0-10 (exclusive)

#use dir. to get more methods
#use help in repl for more