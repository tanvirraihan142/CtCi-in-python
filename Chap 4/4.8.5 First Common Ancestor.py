class Result:
    def __init__(self,n,is_ancestor):
        self.node = n
        self.is_ancestor = is_ancestor
        self.node = None

def common_ancestor(root, p, q):
    r = common_ancestor_helper(root, p ,q )
    if (r.is_ancestor):
        return r.node
    return None

def common_ancestor_helper(root, p, q):
    if root is None:
        return Result(None, False)

    if root==p and root==q:
        return Result(root,True)

    rx = common_ancestor_helper(root.left, p ,q)
    if (rx.is_ancestor):
        return rx

    ry = common_ancestor_helper(root.right, p, q)
    if (ry.is_ancestor):
        return ry

    if (rx.node is not None and ry.node is not None):
        return Result(root,True)
    elif (root==p or root==q):
        is_ancestor = rx.node is not None or ry.node is not None
        return Result(root, is_ancestor)
    else:
        node = rx.node if rx.node is not None else ry.node
        return Result(node, False)

    
        
