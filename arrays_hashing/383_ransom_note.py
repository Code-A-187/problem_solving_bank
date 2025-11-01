# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
from collections import Counter


def can_construct(ransomNote: str, magazine: str) -> bool:

    ransomNote = Counter(ransomNote)
    magazine = Counter(magazine)

    for el in ransomNote:
        if magazine[el] >= ransomNote[el]:
            magazine.pop(el)
        else: return False

    return True

    # Faster Solution

    # for char in set(ransomNote):
    #     if ransomNote.count(char) > magazine.count(char):
    #         return False
    # return True



print(can_construct("azfsg", "bfasgdhzfjkdq"))