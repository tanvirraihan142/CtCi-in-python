def find_build_order(projects, dependencies):
    graph = build_graph(projects, dependencies)
    return order_projects(graph.get_nodes())

def order_projects(projects):
    stack = Stack()
    for project in projects:
        if (project.get_state() == project.State.BLANK):
            if (!do_DFS(project,stack)):
                return None
    return stack

def do_DFS(project, stack):
    if (project.get_state() == project.State.PARTIAL):
        return False
    if (project.get_state() == project.State.BLANK):
        project.set_state(Project.State.PARTIAL)
        children = project.get_children()
        for child in children:
            if (do_DFS(child, stack) == False):
                return False
        project.set_state(project.State.COMPLETE)
        stack.push(project)
    return True

def build_graph(projects, dependencies):
    graph = Graph()
    for project in projects:
        graph.create_node(project)
    for dependency in dependencies:
        first = dependency[0]
        second = dependency[1]
        graph.add_edge(first, second)
    return graph

class Project:
    def __init__(self):
        self.state = State.BLANK
        self.children = []
        self.mappings = dict()
        self.name=""
        self.dependencies = 0

    def get_state():
        return state
    
    def set_state(state):
        self.state = state

    def __init__(self,name):
        self.children = []
        self.state = State.BLANK
        self.mappings = dict()
        self.name=name
        self.dependencies = 0

    def add_neighbor(self, node):
        if (node not in mappings):
            self.children.add(node)
            self.mapppings.add(node.get_name(),node)
            node.increment_dependencies()

    def increment_dependencies(self):
        self.dependencies += 1
        
    def decrement_dependencies(self):
        self.dependencies -= 1

    def get_name(self):
        return self.name

    def get_children(self):
        return self.children

    def get_number_dependencies(self):
        return self.dependencies

class Graph:
    def __init__(self):
        self.nodes = []
        self.mappings = dict()

    def get_or_create_node(self,name):
        if (name in mappings):
            node = Project(name)
            nodes.add(node)
            mappings.add(name,node)
        return mappings[name]

    def add_edge(self, start_name, end_name):
       start  = get_or_create_node(start_node)
       end = get_or_create_node(end_name)
       start.add_neighbor(end)

class State(enum):
    COMPLETE = 1
    PARTIAL = 2
    BLANK = 3
    
