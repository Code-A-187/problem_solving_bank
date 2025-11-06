# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


import re


def is_palindrome(s: str) -> bool:

    # two pointers
    is_alnum = ""
    for el in s.lower():
        if el.isalnum():
            is_alnum += el
    i, j = 0, len(is_alnum) - 1
    while i < j:
        if is_alnum[i] != is_alnum[j]:
            return False
        i += 1
        j -= 1
    
    return True

    # dark magic solution :)

    # is_alnum =  re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # rev_str = is_alnum[::-1]
    # if is_alnum != rev_str:
    #     return False
    # return True

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))