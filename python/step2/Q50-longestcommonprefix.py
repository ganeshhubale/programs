# Longest Common Prefix
# Given an array of strings, find the longest common prefix among all the strings. 
# If no common prefix exists, return an empty string "".

# Time complexity: O(N log N + M)	->  Sorting takes O(N log N), and comparing takes O(M).
# Space complexity: O(N)

def longestCommonPrefix(arr):

    arr.sort()

    result = ""
    for i in range(len(arr[0])):
        if arr[0][i] != arr[-1][i]:
            break
        result += arr[0][i]
    return result

print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""
print(longestCommonPrefix(["interview", "internet", "internal"]))  # Output: "inter"
print(longestCommonPrefix(["a"]))  # Output: "a"
print(longestCommonPrefix(["apple", "ape", "april"]))  # Output: "ap"
print(longestCommonPrefix(["", "anything", "anywhere"]))  # Output: ""
print(longestCommonPrefix(["same", "same", "same"]))  # Output: "same"



# Without sort built in method:

# QuickSort Implementation
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Partition Function for QuickSort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:  # Lexicographic comparison
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to Find Longest Common Prefix
def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Sort the array using QuickSort
    quickSort(strs, 0, len(strs) - 1)

    # Compare the first and last strings after sorting
    first, last = strs[0], strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]

# Test Cases
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""
print(longestCommonPrefix(["interview", "internet", "internal"]))  # Output: "inte"
print(longestCommonPrefix(["a"]))  # Output: "a"
print(longestCommonPrefix(["apple", "ape", "april"]))  # Output: "ap"
print(longestCommonPrefix(["", "anything", "anywhere"]))  # Output: ""
print(longestCommonPrefix(["same", "same", "same"]))  # Output: "same"

