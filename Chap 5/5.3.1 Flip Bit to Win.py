def longest_sequence(n):
	if (n== -1):
		return 4*8
	sequences = get_alternating_sequences(n)
	return find_longest_sequence(sequences)
	
def get_alternating_sequences(n):
	sequences = []
	searching_for = 0
	counter = 0
	
	for i in range(32):
		if ((n&1) != searching_for):
			sequences.add(counter)
			searching_for = n ^ 1
			counter = 0
		counter += 1
		n >>>= 1
	sequences.append(counter)
	return sequences

def find_longest_sequence(seq):
	max_seq = 1
	for i in range(len(seq),2):
		zeros_seq = seq[i]
		ones_seq_right = seq[i-1] if i-1 >= 0 else 0
		ones_seq_left = seq[i+1] if i+1 < len(seq) else 0
		this_seq = 0
		
		if (zeros_seq==1):
			this_seq = ones_seq_left + 1 + ones_seq_right
		elif (zeros_seq >1):
			this_seq = 1 + max(ones_seq_right, ones_seq_left)
		elif (zeros_seq==0):
			this_seq = max(ones_seq_right, ones_seq_left)
		
		max_seq = max(this_seq, max_seq)
	
	return max_seq
	