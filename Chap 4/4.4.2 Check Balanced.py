import sys

MIN_VALUE =-sys.maxsize-1

def check_height(root):
    if (root is None):
        return -1

    left_height = check_height(root.left)
    if (left_height == MIN_VALUE):
        return MIN_VALUE
    right_height = check_height(root.right)
    if (left_height == MIN_VALUE):
        return MIN_VALUE

    height_diff = left_height - right_height

    if (abs(height_diff)>1):
        return MIN_VALUE
    else:
        return max(left_height,right_height)+1

def is_balanced(root):
    return check_height(root) != MIN_VALUE
