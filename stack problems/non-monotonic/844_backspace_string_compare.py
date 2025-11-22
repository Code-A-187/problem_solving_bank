def backspace_compare(s: str, t: str) -> bool:
    # s_stack=[]
    # # backspace first string
    # for el in s:
    #     if el == '#' and s_stack:
    #         s_stack.pop()
    #     elif el != '#':
    #         s_stack.append(el)
    # t_stack = []
    # # backspace first string
    # for el in t:
    #     # if element is # then pop last element from stack
    #     if el == '#' and t_stack:
    #         t_stack.pop()
    #     elif el != "#":
    #         t_stack.append(el)

    # return t_stack == s_stack

    # with function
    def backspaced_string(string):
        string_stack = []
        for el in string:
        # if element is # then pop last element from stack
            if el == '#' and string_stack:
                string_stack.pop()
            # if el is not # append to stack
            elif el != "#":
                string_stack.append(el)
        # return the backspaced string
        return string_stack
        # compare the two backspaced strings returned from the method and return True or False
    return backspaced_string(s) == backspaced_string(t)

print(backspace_compare(s = "ab#c", t = "ad#c")) # True
print(backspace_compare(s = "ab##", t = "c#d#")) # True
print(backspace_compare(s = "a#c", t = "b")) # False
