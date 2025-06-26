class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        str_graph = ""
        for key, value in self.adj_list.items():
            str_graph += f"{key}: {value}\n"
        return str_graph

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists!")

    def add_edge(self, source_node, destination_node, weight=None):
        if source_node not in self.adj_list:
            self.add_node(source_node)
        if destination_node not in self.adj_list:
            self.add_node(destination_node)

        # Add edge with or without weight
        if weight is None:
            self.adj_list[source_node].add(destination_node)
            if not self.directed:
                self.adj_list[destination_node].add(source_node)
        else:
            self.adj_list[source_node].add((destination_node, weight))
            if not self.directed:
                self.adj_list[destination_node].add((source_node, weight))

    def adj_matrix(self, node):
        return self.adj_list.get(node, set())

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]

        while queue:
            current = queue.pop(0)
            if current not in visited:
                print(current, end=" ")
                visited.add(current)
                neighbors = self.adj_list.get(current, [])
                for neighbor in neighbors:
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]  # ignore weight
                    if neighbor not in visited:
                        queue.append(neighbor)

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        print(start_node, end=" "_
