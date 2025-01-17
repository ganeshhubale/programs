# Two Sum
# - Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(nums, target):

    seen = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in seen:
            return f"Sum of {nums[i]} at index {i} and {difference}  at index {seen[difference]} is equal to {target}"
        seen[nums[i]] = i
    return "No target sum found."

nums = [1,2,3,4,5,6,4,5,13]
target = 14
print(two_sum(nums, target))

# Time complexity: O(n)
# Space complexity: O(n) for seen dictionary