# 1.1 Unpacking a Sequence into Separate Variables

#Problem: You have an N-element tuple or sequence that you would like to unpack into a collection of n-variables

#Solution: Any sequence (or iterable) can be unpacked into variables using a simple assignment operation. The only requirement is that the number of variables and structure match the sequence. For example:
	
p = (4, 5)
	
x, y = p
	
print(x)
print(y)
print(x,y)
	 
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)

# Strings
s = 'Hello'
a,b,c,d,e = s
print(a)
print(b)
print(c)
print(d)
print(e)
