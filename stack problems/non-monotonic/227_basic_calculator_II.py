def calculator(s: str) -> int:
    res = []

    # removing all spaces
    s = s.replace(' ','')

    cur_Number = 0
    sign = "+"
    # enumerate the string
    for i, el in enumerate(s):
        if el.isdigit():
            # standart way to get number from string
            cur_Number = 10*cur_Number + int(el)
        # if el not digit or index of or el is last one:
        if el in ("+", "-", "*", "/") or i == len(s) - 1:
            # if plus appedn to stack
            if sign == "+":
                res.append(cur_Number)
            # if minus append curNumber with -
            elif sign == '-':
                res.append(-cur_Number)
            # if multiplication we multiplicatе the last number from stack with cur_Number with 
            elif sign == '*':
                res.append(res.pop() * cur_Number)
            # if devision we division the the last number from stack with the cur_Number
            elif sign == "/":
                p = res.pop()
                res.append(int(p / cur_Number))
            # the sign becomes the current el because it is not digit
            sign = el
            # current number becomes 0
            cur_Number = 0
    # return the sum of the remain numbers because the multiplication and division were done
    return sum(res)


print(calculator("14/3*2"))
print(calculator("3+2*2"))
print(calculator(" 3/2 "))
print(calculator(" 3+5 / 2 "))