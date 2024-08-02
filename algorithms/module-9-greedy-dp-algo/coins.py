def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # Initialize the array for storing the minimum number of coins for each amount
    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0  # Base case: 0 coins needed to make amount 0

    # Array to store the last coin used to make up each amount
    last_coin = [-1] * (amount + 1)

    for coin in coins:
        for current_amount in range(coin, amount + 1):
            if min_coins[current_amount - coin] + 1 < min_coins[current_amount]:
                min_coins[current_amount] = min_coins[current_amount - coin] + 1
                last_coin[current_amount] = coin

    # If the amount cannot be made up by any combination of coins
    if min_coins[amount] == float("inf"):
        return {}

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = last_coin[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result


print(find_min_coins(74))
