def delete_dups(node):
    set1 = set()
    previous = node
    while (node is not None):
        if (node.data in set1):
            previous.next = node.next
        else:
            set1.add(node.data)
            previous = node
        node = node.next
        
