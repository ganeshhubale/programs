# Q6: Write a program to reverse only the vowels in a string.

def reverseVowels(str1):

    s = list(str1)
    start = 0
    end = len(s) - 1
    vowels = set('aeiouAEIOU')
    while start < end:
        while start < end and s[start] not in vowels:
            start +=1
        while start < end and s[end] not in vowels:
            end -= 1
        
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return ''.join(s)

str1 = "leetcodkie"
print(reverseVowels(str1))

# Time complexity - O(n)
# space complexity - O(n)