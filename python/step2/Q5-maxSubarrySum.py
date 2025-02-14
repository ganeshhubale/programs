# Maximum subarry
# Given an integer array nums, find the contiguous subarray (containing at 
# least one number) which has the largest sum, and return the sum.
def max_subarray(nums):
    # Initialize variables
    max_current = max_global = nums[0]
    
    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # Update max_current
        max_current = max(num, max_current + num)
        # Update max_global
        max_global = max(max_global, max_current)
    
    return max_global
    
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray(nums)
print(result)  # Output: 6

# Time complexity : O(n)
# Space complexity : O(1)
