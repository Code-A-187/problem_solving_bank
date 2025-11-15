def length_longest_substring(s: str) -> int:
    longest_substring = ''
    ans = 0

    for char in s:
        while char in longest_substring:
            ans = max(len(longest_substring), ans)
            longest_substring = longest_substring[1:]
        else:
            longest_substring += char

    return max(len(longest_substring), ans)

print(length_longest_substring("aab"))
print(length_longest_substring("bbbbb"))
print(length_longest_substring("pwwkew"))

