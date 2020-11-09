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
        
