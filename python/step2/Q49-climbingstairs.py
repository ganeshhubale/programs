# Climbing Stairs
#     - You are climbing a staircase with N steps. You can climb either 1 step or 2 steps at a time. 
#     Your task is to determine the total number of distinct ways you can reach the top.


# N = 1 > 1

# N = 2 > (1 1), (2)

# N = 3 > (1,1,1) (2,1) (1,2)

# dynamic prgramming
# stepsfor[n] = steps[n-1] + steps[n-2]

def climbStairs(n):

    if n == 1:
        return 1
    if n == 2:
        return 2

    prev2 = 1 # dp [1]
    prev1 = 2 # dp[2]

    for _ in range(3, n+1):
        currentSteps = prev1 + prev2
        prev2 = prev1
        prev1 = currentSteps

    return currentSteps

print(climbStairs(10)) # 89

# Time complexity: o(n)
# Space complexity: o(n)
