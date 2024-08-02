from graph_vizualization import *
from bfs import *
from dfs import *


# DFS and BFS algorithms to find paths
# def dfs_path(graph, start, goal):
#    return list(nx.dfs_edges(graph, source=start, depth_limit=len(graph.nodes)))
#
#
# def bfs_path(graph, start, goal):
#    return list(nx.bfs_edges(graph, source=start))


start_node = "Akademmistechko"
goal_node = "Ipodrom"

dfs_result = dfs_path(G, start_node, goal_node)
bfs_result = bfs_path(G, start_node, goal_node)

print("DFS Path:")
if dfs_result:
    print("DFS path length", len(dfs_result))
    print(" -> ".join(dfs_result))
else:
    print("No path found")

print("\nBFS Path:")
if bfs_result:
    print("BFS path length", len(bfs_result))
    print(" -> ".join(bfs_result))
else:
    print("No path found")

"""
DFS Path:
DFS path length 21
Akademmistechko -> Zhytomyrska -> Sviatoshyn -> Nyvky -> Beresteiska -> Shuliavska -> Politekhnichnyi Instytut -> Vokzalna -> Universytet -> Teatralna -> Zoloti Vorota -> Palats Sportu -> Ploshcha Lva Tolstoho -> Olimpiiska -> Palats Ukraina -> Lybidska -> Demiivska -> Holosiivska -> Vasylkivska -> Vystavkovyi Tsentr -> Ipodrom

BFS Path:
BFS path length 21
Akademmistechko -> Zhytomyrska -> Sviatoshyn -> Nyvky -> Beresteiska -> Shuliavska -> Politekhnichnyi Instytut -> Vokzalna -> Universytet -> Teatralna -> Khreshchatyk -> Maidan Nezalezhnosti -> Ploshcha Lva Tolstoho -> Olimpiiska -> Palats Ukraina -> Lybidska -> Demiivska -> Holosiivska -> Vasylkivska -> Vystavkovyi Tsentr -> Ipodrom

Analysis:
DFS Path:
DFS explores deeply into the graph before backtracking, which can result in paths that are not necessarily the shortest in terms of the number of edges.
BFS Path:
BFS explores nodes level by level, ensuring that the first path found is the shortest path in terms of the number of edges.

With current Kyiv metropoliten graph result are pretty the same in terms of vertex numbers but slightly different with path generated. BFS algo showed more correct result due to it's queue nature.
"""
