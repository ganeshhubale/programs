# Longest Consecutive Sequence

# Given an unsorted array of integers, find the length of the longest sequence of consecutive integers.

# Example: Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive sequence is [1, 2, 3, 4].


# Sort array
# check element sequence

def longestConsecutiveSequence(nums):

    if not nums:
        return 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    i = 1
    max_len = 1
    current_len = 1 # smallest possible sequence where atleast 1 element availble
    for i in range(1, len(nums)):
        # Skip duplicates
        if nums[i] == nums[i-1]:
            i += 1
        elif nums[i] == nums[i-1] + 1:
            current_len += 1
            i+=1

        else:
            max_len = max(max_len, current_len)
            current_length = 1 # sequence break

    return max(max_len, current_length)

print(longestConsecutiveSequence([100,4,200,1,2,3,4,4]))

# Time Complexity: O(n^2) + O(n)
# Space Complexity: O(1)