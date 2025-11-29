from typing import List

def daily_temperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    stack = []

    res = [0] * n

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            index = stack.pop()
            res[index] = i - index

        if i < n:
            stack.append(i)
    
    return res

print(daily_temperatures([73,74,75,71,69,72,76,73]))
print(daily_temperatures([30,40,50,60]))
print(daily_temperatures([30,60,90]))