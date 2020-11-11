last_printed=None

def check_BST(node):
    if node is None:
        return True

    if (check_BST(node.left)==False):
        return False

    if (last_printed is not None and node.data <= last_printed):
        return false

    last_printed = node.data

    if (check_BST(node.right)==False):
        return False

    return True
