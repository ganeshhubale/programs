# Best Time to Buy and Sell Stock
# - You are given an array prices where prices[i] is the price of a given stock on the i-th day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.

def best_time_buy_sell_stock(nums):

    if not nums:
        return 0
    
    min_price = nums[0]
    max_price = 0
    for price in nums:
        min_price = min(min_price, price)
        max_price = max(max_price, price - min_price)
    return f"Profit: {max_price}"

nums = [7,6,5,4,3, 9]
print(best_time_buy_sell_stock(nums))