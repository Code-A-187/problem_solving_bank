# This question is asked by Facebook. 
# Given a string and the ability to delete at most one character, 
# return whether or not it can form a palindrome.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.


def valid_palindrome(s: str) -> bool:
    def is_palindrome(s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return is_palindrome(s, i + 1, j) or is_palindrome(s, i, j - 1)
            
        i += 1
        j -= 1
            
    return True



print(valid_palindrome("abcba"))
print(valid_palindrome("foobof"))
print(valid_palindrome("abccab"))