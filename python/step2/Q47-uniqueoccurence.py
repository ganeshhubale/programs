# Unique Number of Occurrences
#     - The Unique Number of Occurrences problem involves determining whether the frequency of each element 
# in an array is unique. This means no two elements in the array should have the same frequency of occurrence.

# Problem Description
# You are given an integer array arr. Your task is to return True if the number of occurrences 
# of each value in the array is unique. Otherwise, return False.

# Approach
# To solve this problem, follow these steps:

# Count the occurrences:

# Use a dictionary to count the frequency of each element in the array.
# Check uniqueness:

# Use a set to store the frequencies from the dictionary.
# If the size of the set matches the size of the dictionary, all frequencies are unique.

def uniqueOccurrences(nums):

    occurence = {}
    # Step 1: Count the frequency of each element
    for num in nums:
        occurence[num] = occurence.get(num, 0) + 1

    # Step 2: Check if frequencies are unique
    freq_set = set(occurence.values())

    return len(freq_set) == len(occurence.values())

# Example Test Cases
print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # Output: True
# Explanation: Frequencies are {1: 3, 2: 2, 3: 1}, which are unique.

print(uniqueOccurrences([1, 2]))  # Output: False
# Explanation: Frequencies are {1: 1, 2: 1}, which are not unique.

print(uniqueOccurrences([3, 5, -1, -1, 5, 3, 3]))  # Output: False
# Explanation: Frequencies are {3: 3, 5: 2, -1: 2}, which are not unique.

# Time complexity: O(n)
# Space complexity: O(n)