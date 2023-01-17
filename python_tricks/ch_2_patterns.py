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

#In this case, expression1 is the condition we test, and the optional expression2 is an error message that’s displayed if the assertion fails. At execution time, the Python interpreter transforms each assert state- ment into roughly the following sequence of statements:

if __debug__:
    if not expression1:
        raise AssertionError(expression2)

''' Two interesting things about this code snippet:
Before the assert condition is checked, there’s an additional check for the __debug__ global variable. It’s a built-in boolean flag that’s true under normal circumstances and false if optimizations are requested. We’ll talk some more about later that in the “common pitfalls” section.
Also, you can use expression2 to pass an optional error message that will be displayed with the AssertionError in the traceback. This can simplify debugging even further. For example, I’ve seen code like this: '''
if cond == 'x': 
... do_x()

    ... elif cond == 'y': ... do_y()
... else:
...
...
...
...
...
assert False, (
'This should never happen, but it does ' 'occasionally. We are currently trying to ' 'figure out why. Email dbader if you ' 'encounter this in the wild. Thanks!')

