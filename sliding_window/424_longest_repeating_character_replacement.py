from collections import defaultdict


def char_replacement(s: str, k: str) -> int:
    char_freq = defaultdict(int)
    res = 0
    i = 0

    for j in range(len(s)):
        letterJ = s[j]
        char_freq[letterJ] += 1

        max_freq = max(char_freq.values())
        cur_len = j - i + 1
        if cur_len - max_freq > k:
            char_freq[s[i]] -= 1
            i += 1
            cur_len = j - i + 1

        res = max(res, cur_len)
    
    return res

print(char_replacement("ABAB", 2))
print(char_replacement("AABABBA", 1))
# print(char_replacement())