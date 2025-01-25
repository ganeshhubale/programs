# Find the Kth largest element in an array.
# Example:
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5 (The 2nd largest element is 5).


def findkthlargest(nums, k):
    place = k
    k = len(nums) - k

    def quickSelect(l, r):

        pivot, p = nums[r], l

        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        # recursion
        if p > k: return quickSelect(l, p-1)
        elif p < k: return quickSelect(p+1, r)
        else: return f"{nums[p]} is {place}th largest element"

    return quickSelect(0, len(nums)-1)



nums = [3, 2, 1, 5, 6, 4, 99, 78, 55]
k = 4
print(findkthlargest(nums, k))

# Time complexity: O(n) in average case
# but can be o(n^2) in worst case
# Space complexity: O(1)