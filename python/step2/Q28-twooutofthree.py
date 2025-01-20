# Two Out of Three
#     - You are given three integer arrays, nums1, nums2, and nums3. A number is said to appear 
# in two out of the three arrays if it exists in at least two of the arrays.
#     - Your task is to return a list of all such numbers in any order.

def two_out_of_three(nums1, nums2, nums3):

    count_map = {}

    def add_to_map(nums):
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
                count_map[num] = count_map.get(num, 0) + 1
        
    add_to_map(nums1)
    add_to_map(nums2)
    add_to_map(nums3)

    nums_list = [num for num, count in count_map.items() if count >= 2]

    return nums_list

# Example Usage
nums1 = [1, 2, 2, 3]
nums2 = [4, 3, 3, 2]
nums3 = [5, 6, 2, 3]

print(two_out_of_three(nums1, nums2, nums3))  # Output: [2, 3]

# Time complexity: O(n) where n = n1 + n2 + n3 for each array elements
# Space complexity: O(m) where m is the number of distinct numbers across the arrays.


# with set
def two_out_of_three(nums1, nums2, nums3):
    # Convert each array to a set
    set1 = set(nums1)
    set2 = set(nums2)
    set3 = set(nums3)

    # Find numbers that appear in at least two sets
    result = (
        (set1 & set2) |  # Common between set1 and set2
        (set1 & set3) |  # Common between set1 and set3
        (set2 & set3)    # Common between set2 and set3
    )

    # Convert result to a list and return
    return list(result)

# Example Usage
nums1 = [1, 2, 2, 3]
nums2 = [4, 3, 3, 2]
nums3 = [5, 6, 2, 3]

print(two_out_of_three(nums1, nums2, nums3))  # Output: [2, 3]

# Time complexity: O(n) where n = n1 + n2 + n3 for each array elements
# Space complexity: O(n) for sets used

