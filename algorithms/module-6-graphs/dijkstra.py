from graph_vizualization import *


start_node = "Troyeschina"
goal_node = "Ipodrom"

dijkstra_paths = nx.dijkstra_path(G, start_node, goal_node)

print(f"Dijkstra Shortest Path from {start_node} to {goal_node}:")
if goal_node in dijkstra_paths:
    print(" -> ".join(dijkstra_paths))
else:
    print("No path found")

"""
Dijkstra Shortest Path from Troyeschina to Ipodrom:
Troyeschina -> Darnycia -> Zoloti Vorota -> Palats Sportu -> Ploshcha Lva Tolstoho -> Olimpiiska -> Palats Ukraina -> Lybidska -> Demiivska -> Holosiivska -> Vasylkivska -> Vystavkovyi Tsentr -> Ipodrom
"""

# Find shortest paths from all nodes to all nodes
all_pairs_shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

print("\nAll Pairs Shortest Paths:")
for start, paths in all_pairs_shortest_paths.items():
    for goal, path in paths.items():
        print(f"Shortest path from {start} to {goal}: {' -> '.join(path)}")
