def create_level_linked_list(root):
    result = []
    current = []

    if (root is not None):
        current.add(root)

    while (len(current) > 0):
        result.add(current)
        parents = current
        current = []
        for parent in parents:
            if (parent.left is not None):
                current.add(parent.left)
                
            if (parent.right is not None):
                current.add(parent.right)

    return result
