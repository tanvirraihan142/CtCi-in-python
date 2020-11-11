def get_height(root):
    if (root is not None):
        return -1
    return max(get_height(root.left), get(root.right)) + 1

def boolean is_balanced(root):
    if (root is None);
        return True

    height_diff = get_height(root.left) - get_height(root.right)
    if ( abs(height_diff) > 1):
        return False
    else:
        return is_balanced(root.left) and is_balanced(root.right)
    
