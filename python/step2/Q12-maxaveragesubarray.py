# Maximum Average Subarray I
# - You are given an integer array nums consisting of n elements and an integer k.
# Find the maximum average value of any contiguous subarray of size k. You need to 
# return this maximum average as a floating-point number.

# Sliding Window

#steps:
# - get first window sum. that  means sum of first k elements
# - Then assign that to max_sum
# - then itereate array from k to rest elements
# - for each time, add kth element and minus the i-kth element from widnow to maintain k size of subarray
# - then update max_sum comparing widnow sum and current sum
# - return the maximum average that is max_sum / k


def max_average_subarray(nums, k):

    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    max_sum = window_sum

    for i in range(k, len(nums)):

        window_sum += nums[i] - nums[i-k]
        max_sum = max(window_sum, max_sum)

    return max_sum / k

nums = [1, 12, -5, -6, 50, 3]
k = 4
print("Max avaerage of subarray-> ", max_average_subarray(nums, k))

# Time complexity: O(n)
# Space complexity: O(1)