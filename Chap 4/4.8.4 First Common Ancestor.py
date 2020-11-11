def common_ancestor(root, p, q):
    if (root is not None):
        return None
    
    if (root == p or root == q):
        return root

    x = common_ancestor(root.left, p, q)
    if (x is not None and x != p and x!=q):
        return x
    
    y = common_ancestor(root.right,p,q)
    if (y is not None and y != p and y!=q):
        return y

    if (x is not None and y is not None):
        return root
    elif (root == p or root == q):
        return root
    else:
        return y if x is None else x
