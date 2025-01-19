# Subarray Product Less Than K
# Given an array of positive integers nums and an integer k, return the number 
# of contiguous subarrays where the product of all elements in the subarray is less than k.


def subarray_product_less_than_k(nums, k):
    if k <= 1: # No subarray product can be less than 1
        return 0

    start = 0
    end = 0
    count = 0
    product = 1
    pairs = []

    for end in range(len(nums)):

        product = product * nums[end]

        while product >= k and start <= end:
            # remove initial elements
            # means, remove start elements. So product will be reduced to < k
            product = product // nums[start]
            start += 1
        
        # get count of pairs
        count = count + (end - start + 1)

        # get all pairs
        for i in range(start, end+1):
            pairs.append(nums[i:end+1])


    print(f"Total Pairs {count} -> ", pairs)

nums = [10, 5, 2, 6]
k = 100
subarray_product_less_than_k(nums, k)

# Time complexity: O(n^2)
# Space complexity: O(n^2) > Storing the subarrays as pairs requires additional space proportional to the number of valid subarrays.