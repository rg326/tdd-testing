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

def find_sqarea(num):
  sq = num ** 2
  return sq