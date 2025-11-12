def max_vowels(s: str, k: int) -> int:
    res = 0
    max_count = 0

    for i in range(k):
        if s[i] in 'aeiou':
            max_count += 1
    res = max(max_count, res)
    
    for i in range(k, len(s)):
        if s[i] in 'aeiou':
            max_count += 1
        if s[i-k] in 'aeiou':
            max_count -= 1
        
        res = max(res, max_count)
    
    return res

        
print(max_vowels("abciiidef", 3))