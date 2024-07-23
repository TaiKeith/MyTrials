def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in roman_string[::-1]:  # Iterate through the string in reverse
        value = roman_numerals[char]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value
        
    return total

# Test cases
print(roman_to_int("III"))  # Output: 3
print(roman_to_int("IV"))   # Output: 4
print(roman_to_int("IX"))   # Output: 9
print(roman_to_int("LVIII")) # Output: 58
print(roman_to_int("MCMXCIV")) # Output: 1994
print(roman_to_int(None))   # Output: 0
print(roman_to_int(123))    # Output: 0


"""
    The function roman_to_int takes a single argument, roman_string, which is the Roman numeral to be converted to an integer.
    The first thing the function does is check whether roman_string is a valid string and not None. If roman_string is not a string or is None, the function returns 0 as per your requirement.
    This dictionary roman_numerals maps each Roman numeral character to its corresponding integer value.
    total will be used to keep track of the running total of the integer representation of the Roman numeral.
    prev_value stores the value of the previous Roman numeral character encountered. This is used to determine whether the current character should be added or subtracted from the total.
    The loop iterates through each character in the roman_string, starting from the end ([::-1] reverses the string).
    For each character char, the corresponding integer value is retrieved from the roman_numerals dictionary.
    The value is then compared with prev_value. If it's greater than or equal to prev_value, it means that we're building up the total, so we add the value to total.
    If the value is smaller than prev_value, it means that the current value should be subtracted (e.g., "IV" is 5 - 1). So, we subtract the value from total.
    Finally, prev_value is updated to the current value for the next iteration.
    After processing all characters in the roman_string, the function returns the computed total, which is the integer representation of the Roman numeral.
"""
