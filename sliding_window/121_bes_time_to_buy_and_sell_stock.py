from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price =  price
        curr_profit = price - min_price
        if curr_profit > max_profit:
            max_profit = curr_profit


    return max_profit

print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))