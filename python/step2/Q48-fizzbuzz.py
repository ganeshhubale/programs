# Fizz Buzz

# FizzBuzz is a classic programming problem often used in coding interviews. The task is simple:

# Print numbers from 1 to N.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# For multiples of both 3 and 5, print "FizzBuzz".


def fizzBuzz(n):
    output = []
    i = 1
    while i <= n:
        if  i%3 == 0 and i%5 == 0:
            output.append("FizzBuzz")
        elif i%3 == 0:
            output.append("Fuzz")
        elif i%5 == 0:
            output.append("Buzz")
        else: 
            output.append()
        i += 1

    return ', '.join(str(val) for val in output)

print(fizzBuzz(1)) # 1
print(fizzBuzz(3)) # 1, 2, Fizz
print(fizzBuzz(5)) # 1, 2, Fizz, 4, Buzz
print(fizzBuzz(100))

# Time complexity: O(n)
# Space complexity: O(n) for string in list output