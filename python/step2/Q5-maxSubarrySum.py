# Maximum subarry
# Given an integer array nums, find the contiguous subarray (containing at 
# least one number) which has the largest sum, and return the sum.

def max_subarray(nums):

    current_sum = nums[0]
    max_sum = nums[0]
    n = len(nums)

    for i in range(1, n):

        current_sum =  max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

nums = [0, 1, 2, 3, 4, -5, 11]
print(max_subarray(nums=nums))

# Time complexity : O(n)
# Space complexity : O(1)