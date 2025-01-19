# Max Number of K-Sum Pairs

# Given an array of integers nums and an integer k, return the maximum number of pairs (a, b) such that: a + b = k
# Each element in nums can only be used once in a pair.

# hash map

def maxksumpairs(nums, k):
    hashMap = {}
    pairs = []
    # for num in range(len(nums)):
    #     hashMap[nums[num]] = hashMap.get(nums[num], 0) + 1
    
    for num in nums:
        target = k - num
        if target in hashMap and hashMap[target] > 0:
            pairs.append([num, target])
            hashMap[target] -= 1
            # hashMap[num] -= 1
        else:
            hashMap[num] = hashMap.get(num, 0) + 1
    print(f"Total pairs count -> {len(pairs)} and pairs are -> {pairs}")

nums = [1, 2, 3, 4]
k = 5
maxksumpairs(nums, k)