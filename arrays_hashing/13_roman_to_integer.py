def roman_to_int(s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        
        res = 0

        for a, b in zip(s, s[1:]):
                if roman[a] < roman[b]:
                    res -= roman[a]
                else:
                    res += roman[a]

        return res + roman[s[-1]] 



        # with reverse 
        # total = 0
        # pre_value =  0

        # for i in reversed(s):
        #     value = roman[i]

        #     if value < pre_value:
        #         total -= value
        #     else:
        #         total += value

        #         pre_value = value

        # return total

print(roman_to_int("III"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))