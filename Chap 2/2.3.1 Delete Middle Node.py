def delete_node(n):
    if (n is None or n.next is None):
        return False
    next1 = n.next
    n.data = next1.data
    n.next = next1.next
    return True
