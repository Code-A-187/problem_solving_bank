# need to convert given integer to roman symbols.

# will make hash table with {symbol: value} as key-value pair

# will start from left of the int and will append 

# If the value starts with 4 or 9 use the subtractive form representing one symbol 
# subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) 
# less than 10 (X): IX. 

# Only the following subtractive forms are used:
# 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).

# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. 
# You cannot append 5 (V), 50 (L), or 500 (D) multiple times. 
# If you need to append a symbol 4 times use the subtractive form.

def int_to_roman(num: int) -> str:
    # map all symbols we can use from the description above it is list of tuples
    value_symbols = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
    
    # list with symbols for every value in input
    res = []

    # iterate trough list with tuples and we have value and symbol
    for value, symbol in value_symbols:

        # if input is null we break and return empty string
        if num == 0:
            break

        # if num // value it checks how many times the value of that simbol fits in the number without exeeding it. 
        # For example if num is 3549 // 1000 = 3
        count = num // value

        #appends for example "M" symbol 3 times because count is 3. "M" * 3.
        res.append(symbol * count)

        # removes the added provessed value from num. example 3549 - (3 * 1000) = 549
        num -= count * value
        
    return ''.join(res) 

    # BONUS

    # ans=""
    # romans = [
    #         (1000, 'M'),
    #         (900, 'CM'),
    #         (500, 'D'),
    #         (400, 'CD'),
    #         (100, 'C'),
    #         (90, 'XC'),
    #         (50, 'L'),
    #         (40, 'XL'),
    #         (10, 'X'),
    #         (9, 'IX'),
    #         (5, 'V'),
    #         (4, 'IV'),
    #         (1, 'I')
    #     ]
    # for i,j in romans:
    #     while i<=num:
    #         num-=i
    #         ans+=j
    # return ans

print(int_to_roman(3749))
print(int_to_roman(58))
print(int_to_roman(1985))
print(int_to_roman(1994))
print(int_to_roman(2026))
