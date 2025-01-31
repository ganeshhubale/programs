# 11. Implement binary search. - square_root

def sq_root(sq, precision=0.000001):

    if sq < 2:
        return sq
    
    left, right = 0, sq

    while (right-left) > precision:

        mid = left + (right - left) / 2

        if abs(mid*mid - sq) < precision:
            return mid
        elif mid*mid > sq:
            right = mid
        else:
            left = mid
    print(left, right)
    return (left+right) / 2

print("\nSquare root of 25 -> ", sq_root(25))
print("\nSquare root of 17 -> ", sq_root(17))
print("\nSquare root of 99 -> ", sq_root(99))
print("Square root of 0 -> ", sq_root(0))
print("Square root of 1 -> ", sq_root(1))
print("Square root of 9 -> ", sq_root(9))
print("Square root of 225 -> ", sq_root(225))
print("Square root of 224 -> ", sq_root(224))

# Time complexity - O(log2(n/precision))
# Space complexity - O(1)


print("---")

def integer_square_root(x):
    if x < 2:
        return x  # Square root of 0 or 1 is itself

    left, right = 0, x
    result = 0

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid  # Exact square root
        elif mid * mid < x:
            result = mid  # Store the last valid mid
            left = mid + 1
        else:
            right = mid - 1

    return result

# Example usage
x = 17
print(f"Integer square root of {x}: {integer_square_root(x)}")  # Output: 4

# Time complexity - O(logx)
# Space complexity remains - O(1)