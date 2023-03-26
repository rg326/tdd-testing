# Keyword Arguments
# Nonkeyword/Positional Arguments

def area(a, b=4): # Default Param
    return a* b

print(area(b=4, a=5)) #Positional
print(area(a=5, b=7)):
print(area(5, 7))

# Remember, a default param CANNOT come before a non-default param)

#Functions witg an Arbitrary Number of Non-Keyword Arguments
def mean(*args):
    return sum(args)/len(args)

print(mean(1,3,4))
#you get a tuple that contains all the args in the parameter



