from typing import Counter


def min_window(s: str, t: str) -> str:
    # take length of s and t string
    n1, n2 = len(s), len(t)

    if n1 < n2:
        return ""
    # find frq of chars in target(t)
    t_frq = Counter(t)
    # keep track of needed frq chars in  current window
    window_frq = Counter()
    
    # how many met characters (also acurancies) we currently have in count
    have  = 0

    # total unique chars from t
    need = len(t_frq)
    
    #smallest window found with indexes
    res, reslen = [-1, -1], float("infinity")

    # keep track where the left index is
    left = 0

    for right in range(n1):
        # get the current character from the string using the right pointer
        c = s[right]

        # increase the count of this character in the window dictionary
        window_frq[c] += 1
        if c in t_frq  and window_frq[c] == t_frq[c]:
            have += 1
        
        while have == need:
            # if res is less than reslen res is the shortest substring with all chars in t
            if (right - left +1) < reslen:
                res = [left, right]
                reslen = (right - left + 1)
            # we remove one char from window
            window_frq[s[left]] -= 1
            # if char is in t and the window_frq dose not met the needed t_frq we remove one of have and while condition stops
            if s[left] in t_frq and window_frq[s[left]] < t_frq[s[left]]:
                have -= 1
            
            left += 1
        # unpack the found indexes of the min window
    left, right = res
        # we return the window (str) or "" if relsen is not changed because the algorithm couldn't find window
    return s[left:right + 1] if reslen != float("infinity") else ""

print(min_window(s = "AODOBECDEBANC", t = "ABC"))
print(min_window(s = "a", t = "a"))
print(min_window(s = "a", t = "aa"))