class partial_sum:
    def __init__(self):
        sum1 = None
        carry = 0

def add_lists(l1, l2):
    len1 = get_length(l1)
    len2 = get_length(l2)

    if (len1 < len2):
        l1 = pad_list(l1,len2-len1)
    else:
        l2 = pad_list(l2, len1-len2)

    sum1 = add_lists_helper(l1,l2)

    if (sum1.carry == 0):
        return sum1.sum
    else:
        result = insert_before(sum1.sum, sum1.carry)

def add_lists_helper(l1, l2):
    if (l1 is None and l2 is None):
        sum1 = partial_sum()
        return sum1
    
    sum1 = add_list_helper(l1.next,l2.next)
    val = sum1.carry + l1.data + l2.data
    full_result = insert_before(sum1.sum, val%10)
    sum1.sum = full_result
    sum1.carry = val / 10
    return sum1

def insert_before(list1, data):
    node = Node(data)
    if (list1 is not None):
        node.next = list1
    return node

def pad_list(l, padding):
    head = l
    for i in range(padding):
        head = insert_before(head,0)
    return head
