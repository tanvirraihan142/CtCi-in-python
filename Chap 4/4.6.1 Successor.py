def inorder_succ(n):
    if (n is None):
        return None

    if (n.right is not None):
        return left_most_child(n.right)
    else:
        q = n
        x = q.parent

        while (x is not None and x.left != q):
            q = x
            x = x.parent

        return x
        
def left_most_child(n):
    if n is None:
        return None
    while (n.left is not None):
        n = n.left
    return n
