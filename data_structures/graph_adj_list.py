class Graph:
    def __init__(self, directed=False):
        """
        Initializes an empty graph.
        :param directed: Boolean indicating if the graph is directed.
        """
        # Using a dictionary for the adjacency list gives us O(1) vertex lookup
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex):
        """Adds a vertex to the graph if it doesn't already exist."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        """
        Adds an edge from vertex u to vertex v.
        If the graph is undirected, also adds an edge from v to u.
        """
        # Ensure both vertices exist in the graph before adding an edge
        self.add_vertex(u)
        self.add_vertex(v)

        # Add the directed edge
        self.graph[u].append(v)
        
        # If undirected, add the reverse edge to maintain symmetry
        if not self.directed:
            self.graph[v].append(u)

    def display(self):
        """Prints the adjacency list representation of the graph."""
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# --- Quick Test ---
if __name__ == "__main__":
    # Create an undirected graph
    g = Graph(directed=False)
    
    # Add some edges (this will implicitly add the vertices A, B, C, D)
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    
    print("Graph Adjacency List:")
    g.display()