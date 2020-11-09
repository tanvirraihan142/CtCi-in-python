class Result:
    def __init__(self,tail,size):
        self.tail = tail
        self.size = size

def get_tail_and_size(list1):
    if (list1 is None):
        return None
    size1 = 0
    curr = list1
    while (curr.next is not None):
        size += 1
        curr = curr.next
        
    return Result(curr,size)

def get_kth_node(head, k):
    curr = head
    while (k > 0 and curr is not None):
        k-=1
        curr = curr.next
    return curr

def find_intersection(list1, list2):
    if (list1 is None and list2 is None):
        result1 = get_tail_and_size(list1)
        result2 = get_tail_and_size(list2)

        if(result1.tail != result2.tail):
            return None

        shorter = list1 if result1.size < result2.size else list2
        longer = list1 if result1.size > result2.size else list2

        longer = get_kth_node(longer, abs(result1.size - result2.size))
        while(shorter != longer):
            shorter = shorter.next
            longer = longer.next

        return longer
