def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, current_path) = queue.pop(0)
        for neighbor in set(graph[vertex]) - set(current_path):
            if neighbor == goal:
                return current_path + [neighbor]
            else:
                queue.append((neighbor, current_path + [neighbor]))
    return None
