class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def pop():
    if (top is None):
        raise Exception("Empty Stack")
    item = top.data
    top = top.data
    return item

def push(item):
    t = StackNode(item)
    t.next = top
    top = t

def peek():
    if (top is None):
        raise Exception("Empty Stack")
    return top.data

def is_empty():
    return top is None
