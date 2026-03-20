class WeightedGraph:
    def __init__(self, directed=False):
        """
        Initializes an empty weighted graph.
        """
        # Using a nested dictionary: { node: { neighbor: weight } }
        self.graph = {}
        self.directed = directed   

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph if it doesn't already exist.
        """
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, u, v, weight):
        """
        Adds a weighted edge from vertex u to vertex v.
        If the graph is undirected, also adds the reverse edge.
        """
        self.add_vertex(u)
        self.add_vertex(v)
        
        self.graph[u][v] = weight  # Add edge with weight
        
        if not self.directed:
            self.graph[v][u] = weight  # Add reverse edge for undirected graph  


    def get_weight(self, u, v):
        """
        Returns the weight of the edge from u to v, or None if no such edge exists.
        """
        return self.graph.get(u, {}).get(v, None)
    
    def display(self):
        """Prints the adjacency list representation of the graph with weights."""
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")


# --- Quick Test ---

if __name__ == "__main__":
    g = WeightedGraph(directed=False)
    
    # Adding edges with weights: add_edge(u, v, weight)
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    
    print("Weighted Graph Adjacency List:")
    g.display()