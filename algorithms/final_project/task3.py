import heapq


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v, weight))
        # Для неорієнтованого графа додаємо також зворотний шлях
        if v not in self.edges:
            self.edges[v] = []
        self.edges[v].append((u, weight))

    def dijkstra(self, start):
        # Ініціалізація
        min_heap = [(0, start)]
        distances = {vertex: float("inf") for vertex in self.edges}
        distances[start] = 0
        visited = set()

        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)
            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances


# Приклад використання:
graph = Graph()
graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 4)
graph.add_edge("B", "C", 2)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 1)

start_vertex = "A"
distances = graph.dijkstra(start_vertex)

print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Від {start_vertex} до {vertex}: {distance}")

"""
Найкоротші шляхи від вершини A:
Від A до A: 0
Від A до B: 1
Від A до C: 3
Від A до D: 4
"""
