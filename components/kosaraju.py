# "Suppose we have a directed graph G."
# " The maximal subgraph of G in which if there exists a path from vertex v to vertex u, "
# "then there also exists a path from u to v, is called a Strongly Connected Component (SCC). "
# "Problem: Find the SCCs using DFS."


import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_structures.graph_adj_list import Graph

def get_transpose(graph_obj):
    """
    Returns the transpose of a directed graph represented as an adjacency list.
    The transpose of a graph is obtained by reversing the direction of all edges.
    """
    g_transpose = Graph(directed=True)
    adj_list = graph_obj.graph
    
    for u in adj_list:
        g_transpose.add_vertex(u) # Ensure vertex exists even if it has no incoming edges
        for v in adj_list[u]:
            # If u -> v exists in original, add v -> u in transpose
            g_transpose.add_edge(v, u) 
            
    return g_transpose

def fill_order(graph_obj, v, visited, stack):
    """
    Helper function for Step 1: DFS to record finishing times.
    """
    visited.add(v)
    adj_list = graph_obj.graph
    
    for neighbor in adj_list.get(v, []):
        if neighbor not in visited:
            fill_order(graph_obj, neighbor, visited, stack)
            
    # Vertex is finished, push to stack
    stack.append(v)


def dfs_scc(graph_obj, v, visited, current_scc):
    """
    Helper function for Step 3: DFS on transposed graph to collect SCC vertices.
    """
    visited.add(v)
    current_scc.append(v)
    adj_list = graph_obj.graph
    
    for neighbor in adj_list.get(v, []):
        if neighbor not in visited:
            dfs_scc(graph_obj, neighbor, visited, current_scc)


def find_sccs(graph_obj):
    """
    Main function to find and print strongly connected components using Kosaraju's algorithm.
    """
    stack = []
    visited = set()
    adj_list = graph_obj.graph
    
    # Step 1: Perform DFS and fill stack with finishing times
    for i in adj_list:
        if i not in visited:
            fill_order(graph_obj, i, visited, stack)


    # Step 2: create transpose of the graph
    g_transpose = get_transpose(graph_obj)
 
    # Step 3: Perform DFS on transposed graph in order of finishing times
    visited.clear()  # Reset visited for second pass
    all_sccs = []

    while stack:
        # Pop a vertex from stack (this guarantees max finishing time first)
        v = stack.pop()
        if v not in visited:
            current_scc = []
            dfs_scc(g_transpose, v, visited, current_scc)
            all_sccs.append(current_scc)
            
    return all_sccs

# --- Quick Test ---
if __name__ == "__main__":
    # Create a directed graph
    g = Graph(directed=True)
    
    # Adding edges to create 3 distinct Strongly Connected Components
    # SCC 1: A -> B -> C -> A
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'A')
    
    # Cross edge
    g.add_edge('B', 'D')
    
    # SCC 2: D -> E -> F -> D
    g.add_edge('D', 'E')
    g.add_edge('E', 'F')
    g.add_edge('F', 'D')
    
    # Cross edge
    g.add_edge('F', 'G')
    
    # SCC 3: G
    g.add_vertex('G') 

    print("Strongly Connected Components:")
    sccs = find_sccs(g)
    for index, scc in enumerate(sccs, 1):
        print(f"Component {index}: {scc}")