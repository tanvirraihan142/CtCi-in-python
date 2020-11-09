def find_beginning(head):
    slow = head
    fast = head

    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        if (slow==fast):
            break

    if (fast is None or fast.next is None):
        return None

    slow = head
    while (slow is not fast):
        slow = slow.next
        fast = fast.next

    return fast
