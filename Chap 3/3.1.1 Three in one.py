class fixed_multi_stack:
    def __init__(self,stackSize):
        self.number_of_stacks = 3
        self.stack_capacity = stackSize
        self.values = [0 for i in range(self.number_of_stacks*self.stack_capacity)]
        self.sizes = [0 for i in range(self.number_of_stacks)]

    def push(self,stack_num,value):
        if (is_full(stack_num)):
            raise Exception("Full Stack Exception")
        sizes[stack_num]+=1
        values[index_of_top(stack_num)] = value

    def pop(stack_num):
        if (is_empty(stack_num)):
            raise Exception("Empty Stack Exception")
        top_index = index_of_top(stack_num)
        value = values[top_index]
        values[top_index] = 0
        sizes[stack_num]-=1
        return value

    def peek(stack_num):
        if (is_empty(stack_num)):
            raise Exception("Empty Stack Exception")
        return values[index_of_top(stack_num)]

    def is_empty(stack_num):
        return sizes[stack_num]==0

    def is_full(stack_num):
        return sizes[stack_num] == stack_capacity

    def index_of_top(stack_num):
        offset = stack_num * stack_capacity
        size = sizes[stack_num]
        return offset + size - 1
