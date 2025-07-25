class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.grp_dict = {}
        for start, end in self.edges:
            if start in self.grp_dict:
                self.grp_dict[start].append(end)
            else:
                self.grp_dict[start] = [end]
    
    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.grp_dict:
            return []
        
        paths = []
        for node in self.grp_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                if new_paths:
                    for p in new_paths:
                        paths.append(p)
        return paths
    
    
    def shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.grp_dict:
            return None

        shortest = None
        for node in self.grp_dict[start]:  # Fix is here
            if node not in path:
                sp = self.shortest_path(node, end, path)
                if sp:
                    if shortest is None or len(sp) < len(shortest):
                        shortest = sp
        return shortest


if __name__ == '__main__':
    routes = [
        ('Mumbai','Paris'), ('Mumbai','Dubai'), ('Paris','Dubai'), ('Paris','New York'), ('Dubai','New York'), ('New York','Toronto'), ('New York', 'San Fransisco'), ('New York', 'Dallas'), ('Dallas', 'Mumbai'), ('Dallas', 'Rio'), ('Dallas', 'Moscow'), ('Moscow', 'London'), ('Moscow', 'Amsterdam'), ('Rio', 'Cape Town'),('Amsterdam', 'Rio'), ('London', 'Cape Town'), ('Cape Town', 'Boston'), ('Boston', 'New York')
    ]

    route_graph = Graph(routes)
    # print(route_graph.grp_dict)
    start = input("Departure : ")
    end = input("Arrival : ")
    # start = 'Dallas'
    # end = 'Toronto'
    print('All Routes :',route_graph.get_paths(start, end)) 
    print(f'Shortest Route : {route_graph.shortest_path(start, end)}')