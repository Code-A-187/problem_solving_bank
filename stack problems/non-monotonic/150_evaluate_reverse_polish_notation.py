from math import floor, ceil
from typing import List

def eval_rpn(tokens: List[int]) -> int:
    in_tokens =[]
    
    for el in tokens:
        if el == "+":
            t1 = in_tokens.pop()
            t2 = in_tokens.pop()
            in_tokens.append(t2 + t1)
        elif el == "-":
            t1 = in_tokens.pop()
            t2 = in_tokens.pop()
            in_tokens.append(t2 - t1)
        elif el == "*":
            t1 = in_tokens.pop()
            t2 = in_tokens.pop()
            in_tokens.append(t2 * t1)
        elif el =="/":
            t1 = in_tokens.pop()
            t2 = in_tokens.pop()
            in_tokens.append(int(t2/t1))
        else:
            in_tokens.append(int(el))

    return in_tokens.pop()

print(eval_rpn(["4","3","-"]))
print(eval_rpn(["4","13","5","/","+"]))
print(eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))