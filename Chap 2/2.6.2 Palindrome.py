def is_palindrome(head):
    fast = head
    slow = head

    stack = []
    while(fast is not None and fast.next is not None):
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if (fast is not None):
        slow = slow.next

    while(slow is not None):
        top = stack.pop()
        if (top.data != slow.data):
            return False
        slow = slow.next

    return True
