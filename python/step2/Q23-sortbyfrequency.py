# Sort Characters By Frequency
#     - Given a string s, return a string where the characters are sorted 
# by frequency of occurrence in descending order.

def sort_by_frequency(s):

    freq_map = {}
    result = ""
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1

    # Step 2: Convert the frequency map to a list of tuples (char, frequency)
    freq_list = [(char, freq) for char, freq in freq_map.items()]

    # Step 3: Sort the list manually based on frequency in descending order
    for i in range(len(freq_list)):
        for j in range(i + 1, len(freq_list)):
            if freq_list[j][1] > freq_list[i][1]:
                freq_list[i], freq_list[j] = freq_list[j], freq_list[i]

    # Step 4: Build the result string
    result = ""
    for char, freq in freq_list:
        result += char * freq
    
    return result

print(sort_by_frequency("abcc"))

# Time complexity: O(n+k^2) where k is sorting
# Space complexity: O(k) k are the elements in hashmap