import enum

class State(enum.Enum):
    Unvisited=1
    Visited=2
    Visiting=3

def search(g,start,end):
    if (start == end):
        return True

    q = Queue()
    for u in g.get_nodes():
        u.state = State.Unvisited

    start.state = State.Visiting
    q.add(start)
    u = Node()
    while( q.is_empty() == False):
        u = q.remove_first()
        if (u is not None):
            for v in u.get_adjacent():
                if (v==end):
                    return True
                else:
                    v.state = State.Visiting
                    q.add(v)
                    
        u.state = State.Visited
    return False
