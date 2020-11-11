index = 0

def copy_BST(root, array):
    if (root is None):
        return
    copy_BST(root.left, array)
    array[index] = root.data
    index+=1
    copy_BST(root.right, array)

def check_BST(root):
    array = [0 for i in range(root.size)]
    copy_BST(root,array)
    for i in range(len(array)):
        if (array[i] <= array[i-1]):
            return False
    return True
