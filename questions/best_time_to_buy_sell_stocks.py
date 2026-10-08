def best_time_to_buy_sell_stocks(prices: list[int]) -> int:
    size = len(prices)
    assert size >= 2

    max_profit = 0
    for i in range(size - 1):
        for j in range(i + 1, size):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit
