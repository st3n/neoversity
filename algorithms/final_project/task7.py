import random
import matplotlib.pyplot as plt

# Аналітичні ймовірності для двох шестигранних кубиків
analytical_probabilities = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_sum = roll1 + roll2
        sums_count[roll_sum] += 1

    probabilities = {
        sum_val: count / num_rolls for sum_val, count in sums_count.items()
    }
    return probabilities


def plot_probabilities(simulated_probabilities, analytical_probabilities):
    sums = list(range(2, 13))
    simulated = [simulated_probabilities[sum_val] for sum_val in sums]
    analytical = [analytical_probabilities[sum_val] for sum_val in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, simulated, color="blue", alpha=0.6, label="Simulated")
    plt.plot(sums, analytical, color="red", marker="o", label="Analytical")
    plt.xlabel("Sum of Dice Rolls")
    plt.ylabel("Probability")
    plt.title("Simulated vs Analytical Probabilities")
    plt.legend()
    plt.show()


# Параметри симуляції
num_rolls = 100000

# Виконуємо симуляцію
simulated_probabilities = simulate_dice_rolls(num_rolls)

# Виводимо результати
print("Monte Carlo simulated probabilities:")
for sum_val in range(2, 13):
    print(f"Sum {sum_val}: {simulated_probabilities[sum_val]:.4f}")

print("\nAnalytical Probabilities:")
for sum_val in range(2, 13):
    print(f"Sum {sum_val}: {analytical_probabilities[sum_val]:.4f}")

# Створюємо графік
plot_probabilities(simulated_probabilities, analytical_probabilities)

"""
Monte Carlo simulated probabilities:
Sum 2: 0.0277
Sum 3: 0.0545
Sum 4: 0.0831
Sum 5: 0.1094
Sum 6: 0.1411
Sum 7: 0.1663
Sum 8: 0.1393
Sum 9: 0.1111
Sum 10: 0.0834
Sum 11: 0.0553
Sum 12: 0.0288

Analytical Probabilities:
Sum 2: 0.0278
Sum 3: 0.0556
Sum 4: 0.0833
Sum 5: 0.1111
Sum 6: 0.1389
Sum 7: 0.1667
Sum 8: 0.1389
Sum 9: 0.1111
Sum 10: 0.0833
Sum 11: 0.0556
Sum 12: 0.0278                                                                                                                        /18.0s
"""
