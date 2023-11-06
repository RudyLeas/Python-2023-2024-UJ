#code to translate roman numerals to integers
def roman2int(roman):
    roman_digits = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    number = 0
    prev_digit = 0

    for digit in roman:
        if roman_digits[digit] > prev_digit:
            number += roman_digits[digit] - 2 * prev_digit
        else:
            number += roman_digits[digit]
        prev_digit = roman_digits[digit]

    return number

print(roman2int('MMXCIX'))
print(roman2int('MCMXXII'))