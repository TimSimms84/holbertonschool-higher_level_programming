#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    p, ans = 0
    for i in range(len(roman_string) - 1, -1, -1):
        if roman[roman_string[i]] >= p:
            ans += roman[roman_string[i]]
        else:
            ans -= roman[roman_string[i]]
        p = roman[roman_string[i]]
    print(ans)
