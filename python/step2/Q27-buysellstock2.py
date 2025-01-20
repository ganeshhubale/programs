# Best Time to Buy and Sell Stock II

# The problem "Best Time to Buy and Sell Stock II" asks us to maximize the profit by performing 
# multiple transactions

# Input: An array prices where prices[i] is the price of a given stock on the ith day.
# Output: The maximum profit that can be achieved by performing multiple transactions (buy and sell).
# Constraint: You may not engage in multiple transactions simultaneously (i.e., you must sell before you buy again).

# Greedy Algorithm

def maximize_profit_by_buyandsell(prices):
    if len(prices) < 2 or not prices:
        return 0
    
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit = max_profit + (prices[i]-prices[i-1])
    
    return f"Max profit -> {max_profit}" if max_profit > 0 else "No profit"

# Test cases
print(maximize_profit_by_buyandsell([7, 1, 5, 3, 6, 4]))  # Output: 7
print(maximize_profit_by_buyandsell([1, 2, 3, 4, 5]))     # Output: 4
print(maximize_profit_by_buyandsell([7, 6, 4, 3, 1]))     # Output: 0

# Time complexity: O(n)
# Space complexity: O(1)
