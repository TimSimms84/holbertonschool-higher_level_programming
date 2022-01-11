#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return None
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dec, ans = 0, 0
    for i in range(len(roman_string) - 1, -1, -1):
        if roman[roman_string[i]] >= dec:
            ans += roman[roman_string[i]]
        else:
            ans -= roman[roman_string[i]]
        dec = roman[roman_string[i]]
    return(ans)
