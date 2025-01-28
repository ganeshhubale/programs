# Trapping Rain Water
#     - The Trapping Rain Water problem involves calculating
# how much water can be trapped between the heights of bars after a rainstorm.

# Approach
# Two-Pointer Technique:
# Use two pointers (left and right) starting at both ends of the array.
# Track the maximum heights (left_max and right_max) encountered from each side.
# Calculate trapped water based on the lower boundary of the two.

def trap(height):
    if not height: return 0

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water_trapped += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water_trapped += right_max - height[right]
            right -= 1

    return water_trapped

print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Output: 6
# Time: O(n) (single pass with two pointers).
# Space: O(1).