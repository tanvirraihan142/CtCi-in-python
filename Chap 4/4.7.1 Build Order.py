class Project:
    def __init__(self):
        self.children = []
        self.mappings = dict()
        self.name=""
        self.dependencies = 0
        
    def __init__(self,name):
        self.children = []
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


def add_non_dependent(order, projects, offset):
    for project in projects:
        if (project.get_number_dependencies() == 0):
            order[offset] = project
            offset += 1
    return offset

def order_projects(projects):
    order = [i for i in projects]
    end_of_list = add_non_dependent(order, projects, 0)
    to_be_processed = 0
    while (to_be_processed < len(order)):
        current = order[to_be_processed]
        if (current is None):
            return None
        
        children = current.get_children()
        for child in children:
            child.decrement_dependencies()
        end_of_list = add_non_dependent(order, children, end_of_list)
        to_be_processed += 1

    return order
    
def build_graph(projects, dependencies):
    graph = Graph()
    for project in projects:
        graph.create_node(project)
    for dependency in dependencies:
        first = dependency[0]
        second = dependency[1]
        graph.add_edge(first, second)
    return graph

def find_build_order(projects, dependencies):
    graph = build_graoh(projects,dependencies)
    return order_projects(graph.get_nodes())

