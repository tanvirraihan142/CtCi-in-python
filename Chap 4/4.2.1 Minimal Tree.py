def create_minimal_BST(array):
    return create_minimal_tree(array,0,len(array)-1)

def create_minimal_BST(array, start, end):
    if (end < start):
        return None
    mid = (start + end)/2
    n = TreeNode(array[mid])
    n.left = create_minimal_BST(arr,start,mid-1)
    n.right = create_minimal_BST(arr,mid+1,end)
    return n
