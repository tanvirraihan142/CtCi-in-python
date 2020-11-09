def nth_to_last(head,k):
    p1 = head
    p2 = head

    for i in range(k):
        if p1 is None:
            return None
        p1 = p1.next

    while (p is not None):
        p1 = p1.next
        p2 = p2.next

    return p2
