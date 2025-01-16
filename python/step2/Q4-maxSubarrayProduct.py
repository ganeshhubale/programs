# Maximum Product Subarray

# Given an integer array nums, find the contiguous subarray that has 
# the maximum product and return the product.


# Product: Refers to the multiplication operation on subarray elements.
# contiguous (adjucent elements) Subarray: Emphasizes that only contiguous elements are considered.

# for example:
# Array = [2, 3, -2, 4]
# Subarray: [2, 3] → Product: 2 * 3 = 6
# Subarray: [3, -2] → Product: 3 * -2 = -6
# Subarray: [3, -2, 4] → Product: 2 * 3 = 6

# get leftproduct and rightproduct
# get the maximum of it and update
# make sure to assign 1 if leftproduct or rightproduct becomes 0

def maxProductSummary(nums):

    leftProduct = 1
    rightProduct = 1
    n = len(nums)
    result = nums[0]
    for i in range(n):
        if leftProduct == 0:
            leftProduct = 1
        if rightProduct == 0:
            rightProduct = 1

        leftProduct = leftProduct * nums[i]
        rightProduct = rightProduct * nums[n-i-1]

        result = max(result, leftProduct, rightProduct)
    return result

nums = [2, 3, -2, 4]
print(maxProductSummary(nums))

nums = [2, 3, 2, 4]
print(maxProductSummary(nums))

nums = [2, 0, -2, 4]
print(maxProductSummary(nums))

nums = [-2, 0, -2, 4]
print(maxProductSummary(nums))

nums = [-2, 0]
print(maxProductSummary(nums))

# Time complexity: O(n)
# Space complexity: O(1)