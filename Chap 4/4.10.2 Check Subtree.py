def contains_tree(t1, t2):
	if (t2 is None):
		return True
	return sub_tree(t1, t2)
	
def sub_tree(r1, r2):
	if (r1 is None):
		return False
	elif r1.data == r2.data and match_tree(r1, r2)==True:
		return True
	return sub_tree(r1.left, r2) or sub_tree(r1.right, r2)
	
def match_tree(r1, r2):
	if (r1 is None and r2 is None):
		return True
	elif (r1 is None or r2 is None):
		return False
	elif (r1.data != r2.data):
		return False
	else:
		return match_tree(r1.left,r2.left) and match_tree(r1.right, r2.right)
		
	