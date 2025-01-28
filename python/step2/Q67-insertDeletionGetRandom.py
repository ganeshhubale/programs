# Insert Delete GetRandom O(1)
# The problem "Insert Delete GetRandom O(1)" asks you to design a data structure that 
# supports the following operations in constant time:

# Insert(val): Inserts an item val into the data structure. Returns True if the item was not already present, otherwise returns False.
# Remove(val): Removes an item val from the data structure if it exists. Returns True if the item was present, otherwise returns False.
# GetRandom(): Returns a random element from the data structure. Each element must have the same probability of being returned.

# Key Idea:
# To achieve O(1) time complexity for all operations:

# Use a list to store the elements (to efficiently support GetRandom).
# Use a hashmap (dictionary in Python) to store the indices of the elements in the list (to efficiently support Insert and Remove).
import random

class RandomizedSet:
    def __init__(self):
        self.data = []
        self.index_map = {}
    
    def insert(self, data):
        if data not in self.data:
            self.data.append(data)
            self.index_map[data] = len(self.data) - 1
            return True
        return False

    def remove(self, data):
        if data not in self.index_map:
            return False
        
        # Get the index of the element to remove
        index_to_Remove = self.index_map[data]
        last_element = self.data[-1] # get the last element

        # Swap the last element with element to remove index
        self.data[index_to_Remove] = last_element
        print(self.data)
        self.index_map[last_element] = index_to_Remove

        # Now remove the last element from list where we have swapped and pushed it to last
        self.data.pop()
        # delete from hashmap
        del self.index_map[data]
        print(self.data)

        print(self.index_map)

        return True
    def getRandom(self):
        return random.choice(self.data)if self.data else False
    
    
randomized = RandomizedSet()

print("Insert->")
print(randomized.insert(1))
print(randomized.insert(2))
print(randomized.insert(3))
print(randomized.insert(4))
print(randomized.insert(5))
print(randomized.insert(6))

print("remove->")
print(randomized.remove(3))

print("get randome->")
print(randomized.getRandom())

# Time complexity: O(1)
# Space complexity: O(n) for hashmap and list