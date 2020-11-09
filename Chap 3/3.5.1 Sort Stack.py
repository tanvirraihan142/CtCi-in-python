def sort(stack1):
    r = Stack()
    while(stack1.is_empty()):
        temp1 = stack1.pop()
        
        while (r.is_empty()==False and r.peek() > temp1):
            stack1.push(r.pop())
        r.push(temp1)
        
        while (r.is_empty()==False):
            stack1.push(r.pop())
        
            
