def is_valid(s: str) -> bool:
    # stack_s = []
    
    # for el in s:
    #     if el in '([{':
    #         stack_s.append(el)
    #     else:
    #         if not stack_s:
    #             return False
    #         if el == ")" and stack_s[-1] == "(" or el == "]" and stack_s[-1] == "[" or el == "}" and stack_s[-1] == "{":
    #             stack_s.pop()
    #         else:
    #             return False

    # return True if not stack_s else False

    # with dict
        stack_s = []
        check_dict = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if char in check_dict.values():
                  stack_s.append(char)
            elif char in check_dict.keys():
                  if not stack_s or check_dict[char] != stack_s.pop():
                       return False
                  
        return len(stack_s) == 0 

print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([[()]])"))
print(is_valid("([)]"))
