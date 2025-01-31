
# Integer to Roman
# Given an integer num, convert it to a Roman numeral.


# input: 58
# output: 58 = 50 + 5 + 3 → "L" + "V" + "III" → "LVIII"

# greedy algo

# Steps
# Use a list of Roman numerals sorted from largest to smallest.
# Iterate through the list, subtracting values from num and appending the corresponding Roman numeral.
# Repeat until num becomes 0`.

def intToRoman(num: int) -> str:
    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]

    result = []
    
    for value, symbol in roman_map:
        while num >= value:
            result.append(symbol)
            num -= value

    return "".join(result)

print(intToRoman(3))     # Expected Output: "III"
print(intToRoman(58))    # Expected Output: "LVIII"
print(intToRoman(1994))  # Expected Output: "MCMXCIV"
print(intToRoman(3999))  # Expected Output: "MMMCMXCIX"
print(intToRoman(4))     # Expected Output: "IV"
print(intToRoman(9))     # Expected Output: "IX"
print(intToRoman(40))    # Expected Output: "XL"
print(intToRoman(90))    # Expected Output: "XC"
print(intToRoman(400))   # Expected Output: "CD"
print(intToRoman(900))   # Expected Output: "CM"

# Time: O(1) (Max 13 operations) -> The loop never runs more than 13 times, making it constant time.
# Space Complexity: O(1)
# The output does not scale significantly in size.
