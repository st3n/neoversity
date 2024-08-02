import heapq


def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)

    total_cost = 0
    while len(cables) > 1:
        # Витягуємо два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо їх
        new_cable = first + second
        total_cost += new_cable

        heapq.heappush(cables, new_cable)

    return total_cost


# Приклад використання
cables = [4, 3, 7, 6]
print(f"Мінімальні витрати на об'єднання кабелів: {min_cost_to_connect_cables(cables)}")
