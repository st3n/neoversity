# Данні про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо предмети за співвідношенням калорій до вартості у порядку спадання
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            selected_items.append(item)
            total_cost += details["cost"]
            total_calories += details["calories"]

    return selected_items, total_calories


# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    costs = [items[item]["cost"] for item in item_names]
    calories = [items[item]["calories"] for item in item_names]

    # Таблиця для зберігання максимальних калорій для кожного бюджету
    dp = [0] * (budget + 1)
    item_selection = [None] * (budget + 1)

    for i in range(len(items)):
        for w in range(budget, costs[i] - 1, -1):
            if dp[w - costs[i]] + calories[i] > dp[w]:
                dp[w] = dp[w - costs[i]] + calories[i]
                item_selection[w] = i

    total_calories = dp[budget]

    # Відновлюємо вибір предметів
    selected_items = []
    w = budget
    while w > 0 and item_selection[w] is not None:
        item_index = item_selection[w]
        selected_items.append(item_names[item_index])
        w -= costs[item_index]

    return selected_items, total_calories


# Тестові приклади
budget = 100

# Жадібний алгоритм
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print(
    f"Greedy Algorithm: Selected items: {selected_items_greedy}, Total calories: {total_calories_greedy}"
)

# Алгоритм динамічного програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print(
    f"Dynamic Programming: Selected items: {selected_items_dp}, Total calories: {total_calories_dp}"
)
