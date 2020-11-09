class stack_info:
    def __init__(self,start,capacity):
        self.start = start
        self.capacity = capacity
        self.size = 0

    def is_within_stack_capacity(self,index):
        if (index < 0 or index >= value.length):
            return false

        contiguous_index = index + values.length if index < start else index
        end = start + capacity
        return start <= contiguous_index and contiguous_index < end

    def last_capacity_index(self):
        return adjust_index(self.start+self.capacity-1)
    
    def last_element_index(self):
        return adjust_index(self.start+self.size-1)

    def is_full():
        return self.size == self.capacity
    
    def is_empty():
        return self.size == 0
    
class fixed_multi_stack:
    def __init__(self, number_of_stacks,default_size):
        self.info = [stack_info(dafult_size *i, default_size) for i in range(number_of_stacks)]
        values = [0 for i in range(number_of_stacks*default_size)]

    def push(self,stack_num, value):
        if (all_stack_full()):
            raise Exception("Stack OverFlow")
        stack = info[stack_num]
        if (stack.is_full()):
            expand(stack_num)
        stack.size += 1
        values[stack.last_element_index()] = value

    def pop(self,stack_num):
        stack = info[stack_num]
        if (stack.is_empty()):
            raise Exception("Empty Stack")
        value = values[stack.last_element_index()]
        stack.size -= 1
        return value

    def peek(self,stack_num):
        stack = info[stack_num]
        return values[stack.last_element_index()]

    def shift(self,stack_num):
        print("shifting"+str(stack_num))
        stack = info[stack_num]

        if (stack.size >= stack.capacity):
            next_stack = stack_num + 1
            shift(next_stack)
            stack.capacity += 1

        index = stack.last_capacity_index()
        while (stack.is_within_stack_capacity()):
            values[index] = values[previous_index(index)]
            index = previous_index(index)

        values[stack.start] = 0
        stack.start = next_index(stack.start)
        stack.capactiy-=1

    def expand(self,stack_num):
        shift((stack_num+1)%info.length)
        info[stack_num].capacity += 1

    def number_of_elements(self):
        size=0
        for i in info:
            size += i.size
        return size

    def all_stack_are_full(self):
        return number_of_elements() == values.length

    def adjust_index(self,index):
        max1 = values.length
        return ((index%max1)+max1)%max1

    def next_index(self,index):
        return adjust_index(index+1)

    def previous_index(self,index):
        return adjust_index(index-1)
