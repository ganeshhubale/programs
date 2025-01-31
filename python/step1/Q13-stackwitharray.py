# Implement a stack using arrays/linked list.

# with Array 

class stackArray:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def pop(self):
        if self.top >= 0:
            item = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return item
        else:
            raise IndexError("Stack underflow: Cannot pop from an empty stack")

    def push(self, data):
        if self.top < self.capacity - 1:            
            self.top += 1
            self.stack[self.top] = data
    def peak(self):
        if self.top >= 0:
            return self.stack[self.top]
    def size(self):
        return self.top

    def search(self, data):
        if data in self.stack:
            return True
        
    def print(self):
        print("Stack - ", self.stack)

    def is_empty(self):
        return self.top == -1


st = stackArray()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.print()
print("3 Available -> ",st.search(3))
print("Size of stack -> ", st.size())
print("peak of the stack -> ", st.peak())
print("pop of the stack -> ", st.pop())
print("pop of the stack -> ", st.pop())
st.print()

# Time complexity
# Push, Pop, Peak, Size, Is_Empty: O(1)
# Search, Print: O(n)

# Space complexity - O(Capacity)

    