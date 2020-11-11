def common_ancestor(root, p, q):
    if (covers(root, p)==False or cover(root,q)==False):
        return None
    elif (covers(p,q)==True):
        return p
    elif (covers(q,p)==True):
        return q

    sibling = get_sibling(p)
    parent = p.parent
    while (covers(sibling,p)==False):
        sibling = get_sibling(parent)
        parent = parent.parent

    return parent

def covers(root, p):
    if (root is None):
        return False
    if (root == p):
        return True
    return covers(root.left,p) or covers(root.right,p)

def get_sibling(node):
    if (node is None or node.parent is None):
        return None
    parent = node.parent
    return parent.right if parent.left == node else parent.left
