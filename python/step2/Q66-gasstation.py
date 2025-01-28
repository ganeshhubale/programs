# Gas Station
#     - The Gas Station problem is a classic greedy algorithm problem. Here's the problem statement and its solution:
#     - You have n gas stations along a circular route, where the amount of gas at station i is given by gas[i].
# You also have a car with an unlimited gas tank, but it costs cost[i] of gas to travel from station i to station i+1 (the next station).
# You begin the journey with an empty tank at one of the gas stations. Return the starting gas station index if you can travel around the circuit once in the clockwise direction; otherwise, return -1.

# greedy algorithm


def gasStation(gas, cost):

    # If the total gas is less than total cost, it's impossible to complete the circuit
    if sum(gas) < sum(cost):
        return -1
    
    remaining_gas = 0
    start_station = 0
    for i in range(len(gas)):
        remaining_gas = remaining_gas + gas[i] - cost[i]

        if remaining_gas < 0:
            # If tank is negative, reset and start from the next station
            remaining_gas = 0
            start_station += 1
    
    return start_station


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(gasStation(gas, cost))


# Time Complexity: O(n) → A single pass through the gas and cost arrays.
# Space Complexity: O(1) → No additional space is used.