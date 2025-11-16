from typing import Counter

def check_inclusion(s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    # if len s1 bigger than s2 return False
    if n1 > n2: return False

    # store s1_frq and s2_frq with same len
    s1_frq, s2_frq =  Counter(s1), Counter(s2[0:n1])

    # if start of the string is equel return True
    if s1_frq == s2_frq: return True

    # two pointers left and right
    l, r = 0, n1

    # while r is lower than s2 len
    while r < n2:

        # starting to move the window till counters ar equal
        s2_frq[s2[l]] -= 1
        s2_frq[s2[r]] += 1
        if s1_frq == s2_frq:
            return True
        r += 1
        l += 1

    # if not equal counters found return false
    return False

print(check_inclusion(s1 = "ab", s2 = "eidbaooo"))
print(check_inclusion(s1 = "ab", s2 = "eidboaoo"))