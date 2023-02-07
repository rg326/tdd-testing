#Intro to Conditionals

def mean(val):
    if type(val) == dict:
        the mean = sum(val.values() / len(val))
    else:    
        the_mean = sum(myList) / len(myList)
        return the_mean

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
