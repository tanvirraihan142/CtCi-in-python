def partition(node, x):
    head = node
    tail = node

    while (node is not None):
        next1 = node.next
        if (node.data < x):
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next1

    tail.next=None
    return head
