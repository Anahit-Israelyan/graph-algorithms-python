import sys
import os

# This line ensures Python can find the 'data_structures' folder from inside 'traversals'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_structures.graph_adj_list import Graph

def dfs(graph_dict, start_vertex):
    """
    Performs a Depth-First Search on a graph represented as an adjacency list.
    """
    visited = set()

    def _dfs_recursive(current_vertex):
        visited.add(current_vertex)
        print(current_vertex, end=" ")
        
        if current_vertex in graph_dict:
            for neighbor in graph_dict[current_vertex]:
                if neighbor not in visited:
                    _dfs_recursive(neighbor)

    if start_vertex in graph_dict:
        _dfs_recursive(start_vertex)
        print() 
    else:
        print(f"Vertex '{start_vertex}' not found in the graph.")

# --- Quick Test ---
if __name__ == "__main__":
    # 1. Create an instance of your Graph
    g = Graph(directed=False)
    
    # 2. Add some edges to build a test graph
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('B', 'E')
    g.add_edge('B', 'K')
    g.add_edge('K', 'M')
    print("Graph Adjacency List:")
    g.display()
    
    print("\nStarting DFS from vertex 'B':")
    # 3. Call your dfs function, passing in the graph's dictionary (g.graph)
    dfs(g.graph, 'B')