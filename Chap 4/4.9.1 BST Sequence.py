def all_sequences(node):
	result = []
	
	if (node is None):
		result.add([])
		return result
	
	prefix = []
	prefix.add(node.data)
	
	left_seq = all_sequences(node.left)
	right_seq = all_sequences(node.right)
	
	for (left in left_seq):
		for (right in right_seq):
			weaved = []
			weave_lists(left,right,weaved,prefix)
			result.append(i) for i in weaved 
	return result
	
def weave_lists(first, second, results, prefix):
	if (len(first) == 0 and len(second)==0):
		result = copy.deepcopy(prefix)
		result.append(i) for i in first
		result.append(i) for i in second
		results.append(result) 
		
	head_first = first.remove_first()
	weave_lists(first,second,reslts,prefix)
	prefix.remove_last()
	first.add_first(head_first())
	
	head_second = second.remove_first()
	prefix.add_last(head_second)
	weave_lists(first,second,results,prefix)
	prefix.remove_last()
	second.add_first(head_second)
		
		
		