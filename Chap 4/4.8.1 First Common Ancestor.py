def common_ancestor(p, q):
    delta = get_depth(p)-get_depth(q)
    first = delta > 0 ? q : p
    second = delta > 0 ? p : q
    second = go_up_by(second, abs(delta))

    while(first != second and first is not None and second is not None):
        first = first.parent
        second = second.parent

    return None if f(irst is None or second is None) else first


def go_up_by(node, delta):
    while (delta > 0 and node is not None):
        node = node.parent
        delta -= 1
    return node

def get_depth(node):
    depth = 0
    while node is not None:
        node = node.parent
        depth++
    return depth

