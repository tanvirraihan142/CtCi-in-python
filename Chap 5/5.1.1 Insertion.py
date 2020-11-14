def update_bits(n, m, i, j):
	all_ones = ~0
	left = all_ones << (j+1)
	right = ((1<<i)-1)
	mask = left | right
	n_cleared = n & mask
	m_shifted = m << i
	return n_cleared | m_shifted