# Given a string, remove all vowels (both uppercase and lowercase) and 
# capitalize the first letter of each word in the resulting string.
# Input: "AEIOU are vowels"
# Output: "R Vwls"
# Explanation:
# - Remove vowels: "r vwls"
# - Capitalize first letter of each word: "R Vwls"

def remove_vowels(s):

    vowels = "AEIOUaeiou"
    new_str = ''.join([char for char in s if char not in vowels])

    return ' '.join([word.capitalize() for word in new_str.split()])

s = "AEIOU are vowels"
print(remove_vowels(s))