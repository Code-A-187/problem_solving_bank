class Solution(object):
    def is_palindrome(self, s: str):

        s_alpha = ""

        for char in s.lower():
            if char.isalpha():
                s_alpha += char

        i, j = 0, len(s_alpha) - 1

        while i < j:
            if s_alpha[i] != s_alpha[j]:
                return False
            i += 1
            j -= 1

        return True

print(Solution().is_palindrome("A man, a plan, a canal: Panama."))

