def count_bits(digit):
	"""Returns number of set bits in the digit.
	
	Parameters
	----------
	digit: The digit for which number of bits are set.

	Returns
	-------
	integer
		An integer representing number of set bits.

	Example
	-------
	>>> count_bits(7)
	>>> 3
	"""

	num_bits = 0
	
	while digit:
		num_bits += digit & 1
		digit >>= 1

	return num_bits  


if __name__ == "__main__":
	digit = int(input('Enter digit to counts bit for! '))
	result = count_bits(digit)
	print('Number of set bits: ' + str(result))
