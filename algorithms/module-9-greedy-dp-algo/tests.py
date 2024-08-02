from coins import *
import timeit


def test_algorithms(amounts):
    for amount in amounts:
        print(f"\nTesting with amount: {amount}")

        # Тестування жадібного алгоритму
        greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=100)
        greedy_result = find_coins_greedy(amount)
        print(
            f"Greedy algorithm result: {greedy_result}, time: {greedy_time:.6f} seconds"
        )

        # Тестування алгоритму динамічного програмування
        dp_time = timeit.timeit(lambda: find_min_coins(amount), number=100)
        dp_result = find_min_coins(amount)
        print(f"DP algorithm result: {dp_result}, time: {dp_time:.6f} seconds")


# Тестування з великими сумами
amounts = [127, 549, 1168, 5440, 16851, 55555, 196196]
test_algorithms(amounts)
