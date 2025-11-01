# fib
# fibonacci sequence algorithm
# O(2**n)
def fib(n):
    if n <= 2:  #base case
        return 1

    return fib(n - 1) + fib(n - 2)

print(fib(35))

# memoization cash algorithm
# О(n) time - O(n) space
def fib_memoized(n, calculated=None):
    if calculated is None:
        calculated = {1: 1, 2: 1}

    if n in calculated:
        return calculated[n]

    result = fib_memoized(n - 1, calculated) + fib_memoized(n-2, calculated)
    calculated[n] = result

    return result

print(fib_memoized(1000))

# iterable
# O(n) time - O(1) space
def fib_iter(n):
    if n <= 2:
        return 1

    last = 1
    second_last =1

    for i in range(2, n):
        temp = last
        last = last + second_last
        second_last = temp

    return last

print(fib_iter(5000))


# Binary Tree Traversal

class Node:
    def __init__(self, value, left=None, right=None):
        pass


