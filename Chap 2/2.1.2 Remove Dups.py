def delete_dups(node):
    current = node
    while current is not None:
        runner = current
        while (runner.next is not None):
            if (runner.next.data == current.data):
                runner.next = runner.next.next
            else:
                runner = runner.next
            current = current.next
            
