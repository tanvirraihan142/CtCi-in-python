def common_ancestor(root, p, q):
    if (covers(root, p) == False or covers(root,q) == False):
        return None
    return ancestor_helper(root, p ,q)

def ancestor_helper(root, p, q):
    if (root is None or root == p or root == q):
        return root

    p_is_on_left = covers(root.left,p)
    q_is_on_left = covers(root.left,q)

    if (p_is_on_left != q_is_on_left):
        return root

    child_side = root.left is p_is_on_left else root.right
    return ancestor_helper(child_side, p, q)

def covers(root, p):
    if (root is None):
        return False
    if (root == p):
        return True
    return covers(root.left, p) or covers(root.right,p)
