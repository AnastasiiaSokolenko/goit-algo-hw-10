import time
import matplotlib.pyplot as plt

# Жадібний алгоритм
def find_coins_greedy(amount: int) -> dict:
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

# Динамічне програмування
def find_min_coins(amount: int) -> dict:
    coins = [50, 25, 10, 5, 2, 1]
    dp = [0] + [float('inf')] * amount  # dp[i] = мінімальна кількість монет для суми i
    prev = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin

    result = {}
    current = amount
    while current > 0:
        coin = prev[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    # сортування за спаданням номіналів
    return dict(sorted(result.items(), reverse=True))

# Тестові суми
amounts = [100, 113, 500, 1000, 2000, 5000, 10000]

greedy_times = []
dp_times = []

# Обчислення часу виконання та виведення результатів
print(f"{'Amount':>8} | {'Greedy (sec)':>12} | {'DP (sec)':>12} | {'Greedy result':>26} | {'DP result':>26}")
print("-" * 100)

for amount in amounts:
    start = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start
    greedy_times.append(greedy_time)

    start = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start
    dp_times.append(dp_time)

    print(f"{amount:>8} | {greedy_time:12.6f} | {dp_time:12.6f} | {str(greedy_result):>26} | {str(dp_result):>26}")
print("-" * 100 + "\n")

# Побудова графіка
plt.plot(amounts, greedy_times, marker='o', label="Жадібний алгоритм")
plt.plot(amounts, dp_times, marker='o', label="Динамічне програмування")
plt.xlabel("Сума")
plt.ylabel("Час виконання (сек)")
plt.title("Порівняння часу виконання алгоритмів")
plt.legend()
plt.grid(True)
plt.show()