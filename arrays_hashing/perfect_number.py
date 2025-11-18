# A perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its
# positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number
# that is half the sum of all its positive divisors (including itself).

# Write a method that prints the first 4 perfect numbers.

# Perfect Number Example
# 6 = 1 + 2 + 3

from typing import List


def first_four_perfect_numbers() -> List[int]:
    res = []

    start_number = 1

    while len(res) < 4:
        # starting to check every number from 1 up
        curr_sum = 0
    # find all numbers proper positive divisors of the cheked number 
        for i in range(1, start_number):
            # sum all numebers that are proper positive divisors
            if start_number % i == 0:
                curr_sum += i
        # if result is the number we check than the number we are looking at is perfect number 
        if start_number == curr_sum:
            # every number that is perfect number we can put in an array
            res.append(start_number)
        start_number += 1
    # when the array is len 4 the method return these four numbers
    return res
print(first_four_perfect_numbers())

# def first_ten_perfect_numbers():
#     # first ten p such that (2^p - 1) is a Mersenne prime
#     mersenne_p = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127]
#     return [2**(p-1) * (2**p - 1) for p in mersenne_p]

# print(first_ten_perfect_numbers())

# first four perfect number comprehension
# def first_four_perfect_numbers_2():
#     res= []
#     n = 1
#     while len(res) < 4:
#         divisior_sum = sum(i for i in range(1, n) if n % i == 0)

#         if divisior_sum == n:
#             res.append(n)
#         n += 1

#     return res

# print(first_four_perfect_numbers_2())