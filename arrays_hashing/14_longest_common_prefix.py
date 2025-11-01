# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string ""

def longest_common_prefix(strs: list[str])-> str:

    if not strs:
        return ""

    sorted_strs = sorted(strs)
    first_word = sorted_strs[0]
    last_word = sorted_strs[-1]
    longest_prefix = ""

    for i in range(len(first_word)):
        if i < len(last_word) and first_word[i] == last_word[i]:
            longest_prefix += first_word[i]
        else:
            break
    return longest_prefix



print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix([""]))
print(longest_common_prefix(["a"]))
print(longest_common_prefix(["ab", "a"]))
