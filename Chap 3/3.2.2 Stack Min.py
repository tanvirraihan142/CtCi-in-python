import sys

class stack_with_min2(Stack):
    def __init__(self):
        self.s2 = Stack()
        
    def push(value):
        if value <= get_min():
            s2.append(value)
        Stack.push(value)

    def pop():
        value = Stack.pop()
        if (value == get_min()):
            s2.pop()
        return value

    def min():
        if (s2.is_empty()):
            return sys.maxsize
        else:
            s2.peek
