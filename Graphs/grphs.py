class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_str = ""
        for node, neighbour in self.adj_list.items():
            graph_str += f"{node} -> {neighbour}\n"
        return graph_str

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists")
        

    def remove_node(self, node):
        if node not in self.adj_list:
            raise ValueError("Node doesn't exist")
        for neigbours in self.adj_list.values():
            neigbours.discard(node)
        del self.adj_list[node]


    def add_edge(self, from_node, to_node, weight = None):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)
        if weight is None:
            self.adj_list[from_node].add(to_node)
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:   
            self.adj_list[from_node].add((to_node, weight))
            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))
        
        

    def remove_edge(self, from_node, to_node):
        if from_node not in self.adj_list:
            raise ValueError(f"{from_node} does not exist")

        removed = False
    # Handle weighted and unweighted edge removal
        new_neighbors = set()
        for neighbor in self.adj_list[from_node]:
            if (isinstance(neighbor, tuple) and neighbor[0] != to_node) or (isinstance(neighbor, str) and   neighbor != to_node):
                new_neighbors.add(neighbor)
            else:
                removed = True

        if not removed:
            raise ValueError(f"Edge from {from_node} to {to_node} does not exist")

        self.adj_list[from_node] = new_neighbors

    # For undirected graphs: remove reverse edge as well
        if not self.directed:
            if to_node in self.adj_list:
                try:
                    self.remove_edge(to_node, from_node)
                except ValueError:
                    pass  # Ignore if reverse edge already missing
            
    def get_neighbours(self, node):
        return self.adj_list.get(node, set())

    def has_node(self, node):
        return node in self.adj_list

    def has_edge(self, from_node, to_node):
        if from_node in self.adj_list:
            return to_node in self.adj_list[from_node]
        return False

    def get_nodes(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges = []
        for from_nodes, neighbors in self.adj_list.items():
            for to_node in neighbors:
                edges.append((from_nodes,to_node))
        return edges


    def bfs(self, start):
        visited = set()
        queue  = [start]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbours(node)
                for neighbor in neighbors:
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return(order)

    def dfs(self, start):
        visited = set()
        stack  = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbours(node)
                for neighbor in sorted(neighbors, reverse=True):
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return(order)

        

grph1 = Graph(directed=False)
grph1.add_node('Mumbai')
grph1.add_node('Paris')
grph1.add_node('Dubai')
grph1.add_node('New York')
grph1.add_node('Toronto')
grph1.add_node('San Fransisco')
grph1.add_node('Dallas')
grph1.add_node('Boston')
grph1.add_node('London')

grph1.add_edge('Mumbai','New York')
grph1.add_edge('Mumbai', 'Paris')
grph1.add_edge('Mumbai', 'London')
grph1.add_edge('Mumbai', 'Toronto')
grph1.add_edge('Mumbai', 'Dubai')
grph1.add_edge('Mumbai', 'San Fransisco')
grph1.add_edge('New York', 'Boston')
grph1.add_edge('Boston', 'Dallas')
grph1.add_edge('London', 'Dubai')
grph1.add_edge('Toronto', 'Paris')
print(grph1 )

print(grph1.bfs("Mumbai"))
print(grph1.dfs("Mumbai"))
