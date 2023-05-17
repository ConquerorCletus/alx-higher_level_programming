#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    numbers = 0
    roman_numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in reversed(roman_string):
        roman_figures = roman_numerals[i]
        numbers += roman_figures if numbers < roman_figures * 5 else -roman_figures
    return numbers
