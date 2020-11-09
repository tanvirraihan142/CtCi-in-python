def partition(node, x):
    before_start = None
    before_end = None
    after_start = None
    after_end = None

    while (node is not None):
        next1 = node.next
        node.next = None
        if (node.data < x):
            if (before_start is None):
                before_start = node
                before_end = beforfe_start
            else:
                before_end.next = node
                before_end = node
        else:
            if(after_start is None):
                after_start = node
                after_end = after_start
            else:
                after_end.next = node
                after_end = node
        node = next1

    if (before_start == null):
        return after_start

    before_end.next = after_start
    return before_start
