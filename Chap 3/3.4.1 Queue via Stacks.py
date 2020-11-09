class MyQueue:
    def __init__(self):
        stack_newest = Stack()
        stack_older = Stack()

    def size(self):
        return stack_newest.size() + stack_oldest.size()

    def add(self, value):
        stack_newest.push(value)

    def shift_stacks(self):
        if (stack_oldest.is_empty()):
            while(stack_newest.is_empty()):
                stack_oldest.push(stack_newest.pop())

    def peek(self):
        shift_stacks()
        return stack_oldest.peek()

    def remove(self):
        shift_stacks()
        return stack_oldest.pop()
    
