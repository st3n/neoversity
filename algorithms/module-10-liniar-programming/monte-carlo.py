import matplotlib.pyplot as plt
import numpy as np

import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x):
    return x**2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()

# Обчислення інтеграла
integral_quad, _ = spi.quad(f, a, b)

# Метод Монте-Карло
N = 1000000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

# Відсоток точок під кривою
under_curve = y_random < f(x_random)
integral_mc = (b - a) * f(b) * np.sum(under_curve) / N

# Аналітичний розрахунок інтеграла
integral_analytic = (b**3) / 3 - (a**3) / 3

# Виведення результатів
print(f"Метод Монте-Карло: {integral_mc}")
print(f"Аналітичний розрахунок: {integral_analytic}")
print(f"Функція quad: {integral_quad}")

"""
Result:
Метод Монте-Карло: 2.66308
Аналітичний розрахунок: 2.6666666666666665
Функція quad: 2.6666666666666665
Метод Монте-Карло дає результат, близький до аналітичного значення та результату функції quad. Чим більше випадкових точок використовується, тим точніший буде результат Монте-Карло.
Результати дуже близькі з аналітичними, це підтверджує правильність розрахунків.
"""
