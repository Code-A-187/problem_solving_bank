class Solution(object):
    def is_correctly_capitalized(self, word:str):
        if word == "" or word.isupper() or word[0].isupper() and word[1:].islower() or word.islower():
            return True
        else:
            return False

print(Solution().is_correctly_capitalized("2"))