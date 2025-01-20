# String to Integer (atoi)
# - The String to Integer (atoi) function converts a string to a 32-bit signed integer 
# (-2^31 to 2^31 -1) -> (i.e. −2147483648 to 2147483647).
# The function must strip any leading whitespace, handle optional signs, and stop at invalid 
# characters or when the string ends.
# Conditions:
# Remove leading spaces
# Check for + or - sign and result should be depend on it
# stop if you find letter and ignore rest of string
# Result should be within 32 bit signed integer range

def my_atoi(s: str) -> int:

    # Define bounds for a 32-bit signed integer
    INT_MAX = 2**32 - 1
    INT_MIN = -2**31 

    # Initialize variables
    i = 0 
    n = len(s)
    result = 0
    sign = 1

    # step 1: skip leading whitespaces
    while i < n and s[i] == ' ':
        i += 1
    # this will increase the i pointer till it has some letter or digit

    # step 2: check for a sign + or -
    if i < n and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1
        else:
            sign = 1
        # sign is used to finalize result by multiplying result to sign value
        i +=1
        # this will increase the i pointer till it has some letter or digit

    # step 3: convert digits to integer
    while i < n and s[i].isdigit():
        digit = int(s[i])

        # check for overflow or underflow before updating result
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        result = result * 10 + digit
        i +=1
    return sign * result

print(my_atoi("42"))               # Output: 42
print(my_atoi("   -42"))           # Output: -42
print(my_atoi("4193 with words"))  # Output: 4193
print(my_atoi("words and 987"))    # Output: 0
print(my_atoi("-91283472332"))     # Output: -2147483648 (clamped to INT_MIN)
print(my_atoi("+1")) 

# Time complexity: O(n)
# space complexity: O(1)