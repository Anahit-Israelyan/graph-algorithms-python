import sys
import os
import heapq  # We'll use a priority queue (min-heap) for efficient retrieval of the next node with the smallest distance
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_structures.weighted_graph import WeightedGraph


def dijkstra(graph_obj, start_node):
    """
    Finds the shortest path from start_node to all other nodes.
    """
    adj_list = graph_obj.graph
    
    if start_node not in adj_list:
        return "Start node not found."

    # --- INITIALIZATION PHASE ---
    distances = {node: float('inf') for node in adj_list}
    distances[start_node] = 0
    
    visited = set()
    predecessors = {node: None for node in adj_list}

    # --- STATE 2: TO BE VISITED ---
    # The priority queue stores tuples: (current_distance, node_name)
    # It automatically sorts them based on the first item (current_distance)
    pq = [(0, start_node)]

    # --- THE MAIN LOOP ---
    # As long as there are nodes waiting in State 2, keep going
    while pq:
        # 1. Grab the node with the absolute minimum distance l(x')
        # This node transitions into State (3): "Current"
        current_distance, current_node = heapq.heappop(pq)

        # 2. If we have already fully processed this node (State 4), skip it
        if current_node in visited:
            continue
            
        # 3. Mark the node as fully processed (State 4: "Visited")
        visited.add(current_node)

        # 4. For each neighbor of the current node, check if we can improve their distance

        for neighbor, weight in adj_list[current_node].items():
            if neighbor in visited:
                continue  # Skip already visited neighbors
            
            new_distance = current_distance + weight
            
            # If we found a shorter path to the neighbor, update its distance and predecessor
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (new_distance, neighbor))  # Add neighbor to the priority queue
    return distances, predecessors


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
    
    start_node = 'A'
    distances, predecessors = dijkstra(g, start_node)
    
    print(f"\nShortest distances from node '{start_node}':")
    for node, distance in distances.items():
        print(f"Distance to {node}: {distance}")
    
    print("\nPredecessors for each node:")
    for node, pred in predecessors.items():
        print(f"Predecessor of {node}: {pred}")