#  Finding Pairs With a Certain Sum
# - Given an array of integers nums and an integer target, return all unique pairs of numbers in the array that add up to the target.
# You should not use the same element twice, and the order of the pairs does not matter.

def find_pairs_with_certain_sum(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        diff = target - num
        if diff in seen:
            pairs.add(tuple(sorted((num, diff))))
        seen.add(num)
    return [list(pair) for pair in pairs]

nums = [3,3,4,4, 3,4,4,3]
target = 7
print(find_pairs_with_certain_sum(nums, target))

# Time complexity: O(n)
# Space complexity: O(n)