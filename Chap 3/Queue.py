class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

first = QueueNode(0)
last = QueueNode(1)

def add(item):
    t = QueueNode(item)
    if (last is not None):
        last.next = t
    last = t
    if (first is None):
        first = last

def remove():
    if (first is None):
        raise Exception("No such element")
    data = first.data
    first = first.next
    if (first is None):
        last = None
    return data

def peek():
    if (first is None):
        raise Exception("No such element")
    return first.data

def is_empty():
    return first is None
