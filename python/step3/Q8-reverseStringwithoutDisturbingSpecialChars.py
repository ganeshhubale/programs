# reverse String without disturbing position of special chars
#    - Given a string, reverse only the alphabetic characters, while keeping special characters in their original positions.

# Input:  "a,b$c"
# Output: "c,b$a"

# Solution Approach:
# Extract all alphabets from the string.
# Reverse the order of alphabets.
# Replace the original alphabets with reversed ones, while keeping special characters in place

def reverseOnlyChars(str):

    # s = [char for char in str]
    s = list(s)  # Convert string to a list for mutability

    i = 0
    j = len(s) - 1
    while i < j:
        while i < j and not s[i].isalpha():
            i += 1
        while j > i and not s[j].isalpha():
            j -= 1
        s[i], s[j] = s[j], s[i]
        i += 1
        j -=1
    return ''.join(s)

print(reverseOnlyChars("a,b$c")) # c,b$a

# Time complexity: O(n)
# Space: O(m)


# Usig stack
def reverseOnlyChars_stack(s: str) -> str:
    stack = [char for char in s if char.isalpha()]  # Collect all letters in a stack
    result = []

    for char in s:
        if char.isalpha():
            result.append(stack.pop())  # Reverse order using stack
        else:
            result.append(char)  # Keep special characters in place

    return ''.join(result)
print(reverseOnlyChars_stack("a,b$c")) # c,b$a
