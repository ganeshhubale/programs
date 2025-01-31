# Roman to Integer
#     - Given an Roman numeral, convert it to a integer num.

# Left-to-Right Scanning
# Steps
# Use a dictionary to store Roman numeral values.
# Traverse the string s from left to right`.
# If the current numeral is smaller than the next one, subtract it.
# Otherwise, add it to the total sum.


def romanToInt(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s):  # Traverse from right to left
        value = roman_map[char]

        if value < prev_value:
            total -= value  # Subtract if smaller than previous
        else:
            total += value  # Add if greater or equal

        prev_value = value  # Update previous value

    return total

print(romanToInt("III"))     # Expected Output: 3
print(romanToInt("LVIII"))   # Expected Output: 58
print(romanToInt("MCMXCIV")) # Expected Output: 1994
print(romanToInt("IV"))      # Expected Output: 4
print(romanToInt("IX"))      # Expected Output: 9
print(romanToInt("XL"))      # Expected Output: 40
print(romanToInt("XC"))      # Expected Output: 90
print(romanToInt("CD"))      # Expected Output: 400
print(romanToInt("CM"))      # Expected Output: 900
print(romanToInt("MMMCMXCIX")) # Expected Output: 3999



# Time: O(N): We traverse the string once.
# Space: O(1): We use a constant dictionary (roman_map).
