def print_kth_to_last(head,k):
    if (head is not None):
        return -1
    index = print_kth_to_last(head.next,k)+1
    if (index == k):
        print(str(k) + "th item is: "+str(head.data))
    return index
