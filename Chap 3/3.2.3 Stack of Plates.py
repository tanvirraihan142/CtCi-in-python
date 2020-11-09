class set_of_stacks:
    def __init__(self,capacity):
        this.capacity = capacity
        this.stacks = []

    def get_last_stack(self):
        if (len(stacks) == 0):
            return None
        return stacks[-1]

    def push(self, v):
        last = get_last_stack()
        if (last is None and last.is_full() == False):
            last.push(v)
        else:
            stack = Stack(capacity)
            stack.push(v)
            stacks.add(stack)

    def pop(self):
        last = get_last_stack()
        if (last is None):
            raise Exception("Empty Stack")
        v = last.pop()
        if (last.size() == 0):
            stacks.remove(len(stacks)-1)
        return v

    def is_empty(self):
        last = get_last_stack()
        return last is None or last.is_empty()==True

    def pop_at(self,index):
        return left_shift(index,True)

    def left_shift(self, index, remove_top):
        stack = stacks[index]
        removed_item=0
        if (remove_top):
            removed_item = stack.pop()
        else:
            removed_item = stack.remove_bottom()
            
        if (stack.is_empty()):
            stacks.remove(index)
        elif (len(stacks) > index +1):
            v = left_shift(index + 1 , False)
            stack.push(v)
        return removed_item


class Stack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.top = None
        self.bottom = None
        self.size = 0

    def is_full(self):
        return this.capacity==this.size

    def join(self, above, below):
        if below is not None:
            below.above = above
        if above is not None:
            above.below = below

    def push(self, v):
        if (self.size >= self.capacity):
            return False
        self.size += 1
        n = Node(v)
        if (self.size == 1):
            self.bottom = n
        join(n, self.top)
        self.top = n
        return True

    def pop():
        t = top
        self.top = self.top.below
        self.size -= 1
        return t.value

    def is_empty():
        return self.size==0

    def remove_bottom():
        b = self.bottom
        self.bottom = self.bottom.above
        if (bottom is not None):
            bottom.below = None
        self.size -= 1
        return b.value
    
        
        
