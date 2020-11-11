def create_level_linked_list(root, lists, level):
    if (root is None):
        return
    list1 = None

    if (len(lists) == level):
        list1 = []
        lists.append(list1)
    else:
        list1 = lists[level]

    list1.add(root)
    create_level_linked_list(root.left,lists,level+1)
    create_level_linked_list(root.right,lists,level+1)

def create_level_linked_list(root):
    lists = []
    create_level_linked_list(root,lists,0)
    return lists
