class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def append_to_tail(self, d):
        end = Node(d)
        n = self
        while (n.next is not None):
            n = n.next
        n.next=end

    
def deleteNode(head, d):
    n = head
    if (n.data == d):
        return head.next
    while (n.next != null):
        if (n.next.data == d):
            n.next = n.next.next
            return head
        n = n.next
    return head
