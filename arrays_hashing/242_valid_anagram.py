# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def is_anagram(s: str, t: str) -> bool:
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))

    if s == t:
        return True
    else:
        return False

    # second Solution
    # return Counter(t) == Counter(s)


print(is_anagram("aacc", "ccac"))