def is_palindrome(head):
    reversed_list=reverse_and_clone(head)
    return is_equal(head,reversed_list)

def reverse_and_clone(node):
    head = None
    while (node is not None):
        n = Node(node.data)
        n.next = head
        head = n
        node = node.next
    return head

def is_equal(list_one, list_two):
    while(list_one is not None and list_two is not None):
        if (list_one.data != list_two.data):
            return false
        list_one = list_one.next
        list_two = list_two.next
    return list_one is not None and list_two is not None
