class Result:
    def __init__(self):
        self.node = None
        self.result = False

def is_palindrome(head):
    length = length_of_list(head)
    p = is_palndrome_recurse(head,length)
    return p.result

def is_palindrome_recurse(head,length):
    if head is None or length <= 0:
        return Result(head,True)
    elif (length == 1):
        return Result(head.next,True)

    res = is_palindrome_recurse(head.next,length-2)
    if (res.result == False or res.Node is None):
        return res
    res.result = (head.data == res.node.data)
    res.node = res.node.next
    return res

def length_of_list(node):
    size = 0
    while(n is not None):
        size += 1
        n = n.next
    return size
