#The "Minimum Operations to Reduce X to Zero" problem involves finding the minimum number 
# of operations required to reduce a given integer  X to zero by removing elements from the ends of an array. 
# This is a common sliding window problem in algorithmic problem-solving.

# Input:
# An array of positive integers nums.
# An integer X.
# Output:
# The minimum number of operations to reduce X to 0. If it is not possible, return -1.
# Operations:
# You can remove elements from either the start or the end of the array.

def minimum_op_reduce_X_to_Zero(nums, x):

    target = sum(nums) - x
    if target < 0:
        return -1 # Impossible to reach x
    
    current_sum = 0
    max_window = -1
    l = 0

    for r in range(len(nums)):
        current_sum += nums[r]

        while current_sum > target and l <= r:
            current_sum -= nums[l]
            l +=1
        
        if target == current_sum:
            max_window = max(max_window, r-l+1)
        
    return -1 if max_window == -1 else len(nums) - max_window

print(minimum_op_reduce_X_to_Zero([1, 1, 4, 2, 3], 5)) # Output: 2
print(minimum_op_reduce_X_to_Zero([5, 6, 7, 8, 9], 4))  # Output: -1
print(minimum_op_reduce_X_to_Zero([3, 2, 20, 1, 1, 3], 10))  # Output: 5

# Time complexity: O(n)
# Space complexity: O(1)