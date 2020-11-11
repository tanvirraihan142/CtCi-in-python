def count_paths_with_sum(root, target_sum):
	dict1 = dict()
	return count_paths_with_sum(root, target_sum, 0, dict1)
	
def count_paths_with_sum(node, target_sum, running_sum, path_count):
	if (node is None):
		return 0
	
	running_sum += node.data
	sum1 = running_sum - target_sum
	total_paths = path_count[sum1] if sum1 in path_count else 0
	
	if (running_sum = target_sum):
		total_paths += 1
	
	increment_hash_table(path_count, running_sum, 1)
	total_paths += count_paths_with_sum(node.left, target_sum, running_sum, path_count)
	total_paths += count_paths_with_sum(node.right, target_sum, running_sum, path_count)
	increment_hash_table(path_count, running_sum, -1)
	
	return total_paths
	
def increment_hash_table(hash_table, key, delta):
	new_count = path_count[key] if key in path_count else 0
	new_count += delta
	if (new_count == 0):
		del path_count[key]
	else:
		path_count[key] = new_count
	