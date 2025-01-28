# Valid Parentheses
#     - Given a string containing just the characters 
# '(', ')', '{', '}', '[', ']', determine if the input string is valid.
# A string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Input: "()" → Output: True
# Input: "()[]{}" → Output: True
# Input: "(]" → Output: False
# Input: "([)]" → Output: False
# Input: "{[]}" → Output: True

# Use stack

def validParenthesis(parenth):
    stack = []
    x_dict = {"}": "{", "]": "[", ")": "("}

    for p in parenth:
        if p in x_dict:
            # Pop the top element of the stack if it's not empty; otherwise use a dummy value
            top_element = stack.pop() if stack else "#"

            # If the mapping for the closing bracket doesn't match the stack's top, return False
            if x_dict[p] != top_element:
                return False
        else:
            stack.append(p)

    return "Valid" if not stack else "Not valid"

print(validParenthesis("()[]{}"))

# Time Complexity: O(n)
# Space Complexity: O(n): In the worst case (e.g., "(((((("), the stack could store all the opening brackets.
