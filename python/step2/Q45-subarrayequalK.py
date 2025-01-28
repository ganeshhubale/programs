# Given an integer array nums and an integer k, return the total number of 
# continuous subarrays whose sum equals k.

# Key Idea:
# Maintain a running sum as you iterate through the array.
# For each element, check if there exists a subarray with a sum equal to k. You can do this by storing the prefix sums in a hash map (or dictionary). The idea is:
# current_sum = prefix_sum[i] (sum of elements from the start to the current element).
# The subarray sum that ends at the current element and equals k is given by: current_sum−k
# If current_sum - k has appeared before in the hash map, it means there exists a subarray that ends at the current index and has a sum equal to k.
# The hash map stores the frequency of each running sum encountered so far.

# hash maps

def subarrayEqualK(nums, k):
    prefix_sum_map = {}
    prefix_sum_map[0] = 1
    current_sum = 0
    count = 0
    for num in nums:
        current_sum += num

        # if current_sum - k in prefix_sum_map:
        count += prefix_sum_map.get(current_sum - k, 0)
            
        prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) + 1 

    return count
# Test case
nums = [1, 1, 1]
k = 2
print(subarrayEqualK(nums, k))

# Time Complexity: O(n)
# Space Complexity: O(n)
