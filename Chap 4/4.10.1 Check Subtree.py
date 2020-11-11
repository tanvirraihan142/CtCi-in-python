def contains_tree(t1, t2):
	string1 = []
	string2 = []

	get_order_string(t1, string1)
	get_order_string(t2, string2)
	
	return string2 in string1
	
def get_order_string(node, stringer):
	if node is None:
		stringer.append("X")
		return
	stringer.append(str(node.data) + " ")
	get_order_string(node.left, stringer)
	get_order_string(node.right, stringer)
	
	