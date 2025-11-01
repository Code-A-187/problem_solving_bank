# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagram_map[sorted_str].append(s)

        return list(anagram_map.values())



print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
print(group_anagrams([""]))