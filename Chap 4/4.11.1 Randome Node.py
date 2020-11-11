from random import random

class TreeNode:
	def __init__(self, d):
		self.data = d
		self.size = 1
		self.left = None
		self.right = None
		
	def get_random_node(self):
		left_size = 0 if self.left is None else self.left.get_size()
		random = random()
		index = randint(0,size)
		if (index < left_size):
			return left.get_random_node()
		elif (index == left_size):
			return self
		else:
			return right.get_random_node()
			
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
		