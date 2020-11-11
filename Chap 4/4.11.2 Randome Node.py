from random import random

class Tree:
	def __init__(self):
		self.root = None
		
	def get_size(self):
		return 0 if self.root is None else root.get_size()
		
	def insert_in_order(self, value):
		if root is None:
			root = TreeNode(value)
		else:
			root.insert_in_order(value)
			
	def get_random_node(self):
		if (root is None):
			return None
		i = random(get_size())
		return root.get_ith_node(i)
		
class TreeNode:
	def __init__(self, d):
		self.data = d
		self.size = 1
		self.left = None
		self.right = None
	
	def get_ith_node(i):
		left_size = 0 if left is None else left.get_size()
		if (i < left_size):
			return left.get_ith_node(i)
		elif (i == left_size):
			return self
		else:
			return right.get_ith_node(i-(left_size+1))
	
	def insert_in_order(d):
		if (d <= data):
			if (self.left is None):
				left = TreeNode(d)
			else:
				left.insert_in_order(d)
		else:
			if (right is None):
				right = TreeNode(d)
			else:
				right.insert_in_order(d)
		self.size += 1
		
	def get_size():
		return self.size
		
	def get_data():
		retunr self.data
	
	def find(d):
		if (d==self.data):
			return self
		elif (d<=data):
			return left.find(d) if self.left is not None else None
		elif (d>data):
			return right.find(d) if left.right is not None else None
		return None