def bit_swap_required(a, b):
	count = 0
	c = a ^ b
	while (c!=0):
		count += c&1
		c >>= 1
	return count