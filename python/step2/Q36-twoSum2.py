
# Two Sum II - Input Array Is Sorted
#     - Given a 1-indexed sorted array of integers numbers and a target integer target,
#      return the indices of the two numbers that add up to target.The solution must satisfy the following constraints:

# Each input has exactly one solution, and you may not use the same element twice.
# The indices returned should be in ascending order.

# Input:
# numbers = [2, 7, 11, 15], target = 9

# Output:
# [1, 2]
# Explanation: numbers[0] + numbers[1] = 2 + 7 = 9.

# Two pointer

def twoSumIndices(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        elif sum == target:
            return [left+1, right+1]
            
    return "Target sum not found"

nums = [2, 7, 11, 15, 35, 66]
target = 9
print(twoSumIndices(nums, target))

# Time complexity: O(n)
# Space complexity: O(1)