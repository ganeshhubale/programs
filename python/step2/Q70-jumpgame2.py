# Jump game 2

# The Jump Game II problem is a variation of the original Jump Game. In this version, 
# you must determine the minimum number of jumps required to reach the last index.

# You are given an array of non-negative integers nums, where each 
# element represents your maximum jump length at that position. 
# Your task is to find the minimum number of jumps needed to reach the last index.

# Example:
# Input:
# nums = [2, 3, 1, 1, 4]

# Output:
# 2

# Explanation:
# Start at index 0, with value 2. You can jump to index 1 or 2. Jump to 1.

# Greedy Algorithm

def minJumpGame(nums):
    current_jump_end = 0
    minJumps = 0
    farthest = 0

    for i in range(len(nums) - 1): # 
        farthest  = max(farthest, nums[i] + i)
        if i == current_jump_end: # When you reach the end of the current jump range
            minJumps += 1 # This is count of jump need to reach at this index
            current_jump_end  = farthest # Move to the next jump range
    return minJumps

nums = [2, 3, 1, 1, 4]
print(minJumpGame(nums))

# Time complexity: O(n)
# Space Complexity: O(1)