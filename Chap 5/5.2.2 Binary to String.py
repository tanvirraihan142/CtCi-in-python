def print_binary2(num):
	if (num >= 1 || num <= 0):
		return "ERROR"
		
	binary = []
	frac = 0.5
	binary.append(".")
	
	while (num > 0):
		if (len(binary)>32):
			return "ERROR"
		if (num >= frac):
			binary.append("1")
			num -= frac
		else:
			binary.append("0")
		frac /= 2
	return "".join(binary)