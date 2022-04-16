# Chapter 4 1.1

def count_bits(x: int) -> int:
	num_bits = 0
	while x:
		num_bits += x & 1
		x >>= 1
	return num_bits
	
	# https://realpython.com/python-bitwise-operators/
