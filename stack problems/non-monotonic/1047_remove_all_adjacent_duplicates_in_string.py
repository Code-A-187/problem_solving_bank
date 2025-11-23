def remove_duplocates(s: str) -> str:
    # initial stack
    greedy_stack = []

    # for loop in s for every char
    for char in s:
        # if there is something in stack and current char is equal to the last el in stack, then pop the last element from stack.
        if greedy_stack and char == greedy_stack[-1]:
            greedy_stack.pop()
        else:
        # if last el is not equal to current char, append char to the end of stack
            greedy_stack.append(char)
        
    # return the stack as str 
    return "".join(greedy_stack)

print(remove_duplocates(s = "abbaca"))
print(remove_duplocates(s = "azxxzy"))

