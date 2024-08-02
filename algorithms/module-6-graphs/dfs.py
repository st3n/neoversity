# DFS and BFS algorithms to find paths
def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, current_path) = stack.pop()
        for neighbor in set(graph[vertex]) - set(current_path):
            if neighbor == goal:
                return current_path + [neighbor]
            else:
                stack.append((neighbor, current_path + [neighbor]))
    return None
