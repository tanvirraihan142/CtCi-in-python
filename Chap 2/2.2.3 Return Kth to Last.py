class index:
    def __init__(self):
        self.value=0

def kth_to_last(head,k):
    idx = index()
    return kth_to_last(head,k,idx)

def kth_to_last(head,k,idx):
    if head is None:
        return None
    node = kth_to_last(head.next,k,inx)
    idx.value += 1
    if (idx.value == k):
        return head

    return node
    
