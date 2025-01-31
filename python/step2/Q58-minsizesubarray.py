# Minimum Size Subarray Sum
#     - Given an array of positive integers nums and an
# integer target, return the minimum length of a contiguous subarray whose sum is greater than or equal to target.
#     If no such subarray exists, return 0.


#  SLIDING WINDOW

def minSubArrayLen(target: int, nums: list[int]) -> int:
    left = 0
    current_sum = 0
    min_length = float("inf") # or len(nums) + 1 and handle it while returning

    for right in range(len(nums)):
        current_sum += nums[right]  # Expand the window

        # Shrink the window as much as possible while sum >= target
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]  # Shrink the window from left
            left += 1  # Move left pointer

    return min_length if min_length != float("inf") else 0  # If no subarray found, return 0

print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # Expected Output: 2
print(minSubArrayLen(4, [1, 4, 4]))  # Expected Output: 1
print(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # Expected Output: 0
print(minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))  # Expected Output: 2
print(minSubArrayLen(20, [2, 3, 1, 2, 4, 3]))  # Expected Output: 0


# Time ComplexitY : O(N)	
# Space Complexity: O(1)