def swap_odd_even_bits(x):
	a = (x & int("0xAAAAAAAA",16)) >>> 1
	b = (x & int("0x55555555",16)) >>> 1
	return a | b