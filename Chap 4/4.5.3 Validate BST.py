def check_BST(n):
    return check_BST(n, None, None)

def check_BST(n, min1, max1):
    if (n is None):
        return True

    if (n.data <= min1) or (n.data >= max1):
       return False

    if (check_BST(n.left,min1,n.data)==False or check_BST(n.right, n.data, max1)==False:
        return False

    return True
