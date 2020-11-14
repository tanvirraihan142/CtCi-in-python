def print_binary(num):
	if (num >= 1 || num <= 0):
		return "Error"
	binary = []
	binary.append(".")
	
	while (num > 0):
		if (len(binary)>0):
			r = num * 2
			if (r >= 1):
				binary.append("1")
				num = r -1
			else:
				binary.append("0")
				num = r
	return "".join(binary)
	
	
	