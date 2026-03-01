import sys
import os

# This line ensures Python can find the 'data_structures' folder from inside 'traversals'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_structures.graph_adj_list import Graph

def bfs(graph_dict, start_vertex):
    """
    Performs a Breadth-First Search on a graph represented as an adjacency list.
    """
    visited = set()
    queue = [start_vertex]

    while queue:
        current_vertex = queue.pop(0)  # Dequeue the first vertex
        
        if current_vertex not in visited:
            visited.add(current_vertex)
            print(current_vertex, end=" ")
            
            # Enqueue all unvisited neighbors
            if current_vertex in graph_dict:
                for neighbor in graph_dict[current_vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    print()  # For a newline after traversal    
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
    g.add_edge('M', 'P')  
    g.add_edge('M', 'U')  
    g.add_edge('P', 'Q')  
    print("Graph Adjacency List:")
    g.display()
    
    print("\nStarting BFS from vertex 'B':")
    # 3. Call your bfs function, passing in the graph's dictionary (g.graph)
    bfs(g.graph, 'B')
