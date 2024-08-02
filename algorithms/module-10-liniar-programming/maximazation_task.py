import pulp

model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Змінні рішення
x = pulp.LpVariable("Lemonade", lowBound=0, cat="Continuous")
y = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Continuous")

# Цільова функція
model += x + y, "Total_Production"

# Обмеження
model += 2 * x + 1 * y <= 100, "Water_Constraint"
model += x <= 50, "Sugar_Constraint"
model += x <= 30, "Lemon_Juice_Constraint"
model += 2 * y <= 40, "Fruit_Puree_Constraint"

model.solve()

print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade production: {pulp.value(x)} units")
print(f"Fruit Juice production: {pulp.value(y)} units")
print(f"Total Production: {pulp.value(model.objective)} units")
