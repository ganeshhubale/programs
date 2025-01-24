# Remove K Digits
#     - To remove exactly k digits from a given non-negative number represented as
#  a string to make the resulting number as small as possible.

# Input:
# A non-negative integer as a string num.
# An integer k, the number of digits to remove.

# Output:
# The smallest possible number (as a string) after removing k digits.

# Rules:
# The resulting number should not have leading zeroes.
# If the number becomes empty, return "0".

# Greedy Algorithm with stack

# Steps:
# Iterate through each digit in the number.
# Use a stack to build the smallest number:
# While the current digit is smaller than the top of the stack and you still need to remove digits (k > 0), pop the stack.
# Push the current digit onto the stack.
# After processing all digits:
# If k > 0, remove additional digits from the end of the stack.
# Remove any leading zeroes from the resulting stack.
# If the stack is empty, return "0"; otherwise, return the number formed by the stack.


def removekdigits(nums, k):

    stack = []

    for digit in nums:
        while stack and k > 0 and stack[-1] > digit:
            k -= 1
            stack.pop()
        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1

    # remove leading zeros
    result = ''.join(stack).lstrip('0')
    # result = ''.join(stack)
    # i = 0
    # while i < len(result) and result[i] == '0':
    #     i += 1

    return result if result else '0'

print(removekdigits("1432219", 3))
print(removekdigits("10200", 1))
print(removekdigits("10", 2))

# Time complexity: O(n)
# Space complexity: O(n)
