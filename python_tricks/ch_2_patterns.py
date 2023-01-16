#Assertions
# Use assertions to help automatically detect errors in python

#Example 1
def apply_discount(product, discount):
price = int(product['price'] * (1.0 - discount)) assert 0 <= price <= product['price']
return price
>>> shoes = {'name': 'Fancy Shoes', 'price': 14900}

#Example 2
>>> apply_discount(shoes, 2.0) Traceback (most recent call last):
File "<input>", line 1, in <module> apply_discount(prod, 2.0)
File "<input>", line 4, in apply_discount assert 0 <= price <= product['price']

#As you can see, when we try to apply this invalid discount, our program halts with an AssertionError. This happens because a discount of 200% violated the assertion condition we placed in the apply_discount function.

#Assert syntax
assert_stmt ::= "assert" expression1 ["," expression2]

