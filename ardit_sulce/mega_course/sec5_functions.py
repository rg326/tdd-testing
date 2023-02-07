#Mean Function

def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

  print(mean([1, 4, 6]))  
  print(type(mean), type(sum))

  # Currency Converter Function
  def convert(amount):
    output = amount * 1.75
    return output

print(convert(10))

#Func Exercise 1
def find_sqarea(num):
  sq = num ** 2
  return sq

#Func Evercise 2
def volconvert(amount):
  new_vol = amount * 29.57353
  return new_vol