# input : "manojpandey" , ouptp: a:2, n: 2 , "manojpdey"

def uniqueChars(s):

    if not s:
        return False
    
    x = {}
    new_string = ''
    for char in s:
        if char not in new_string:
            new_string += char 
        x[char] = x.get(char, 0) + 1

    return ':'.join([char for char, values in x.items() if values>1]), new_string

print(uniqueChars("manojpandey"))

# Time complexity: O(n)
# Space complexity: O(m)