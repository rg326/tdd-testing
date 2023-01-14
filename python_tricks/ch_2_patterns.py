#Assertions
# Use assertions to help automatically detect errors in python

def apply_discount(product, discount):
price = int(product['price'] * (1.0 - discount)) assert 0 <= price <= product['price']
return price
>>> shoes = {'name': 'Fancy Shoes', 'price': 14900}