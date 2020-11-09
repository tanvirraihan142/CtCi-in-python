def add_lists(l1, l2, carry):
    if (l1 is None and l2 is None and carry==0):
        return None

    result = Node()
    value = carry
    if (l1 is not None):
        value += l1.data
    if (l2 is not None):
        value += l2.data

    result.data = value % 10
    
    l1_next = None if l1 is None else l1.next
    l2_next = None if l2 is None else l2.next
    value = 1 if value >=0 else 0

    if (l1 is not None or l2 is not None):
        more = add_lists(l1_next,l2_next,value)
        result.set_next(more)

    return result
