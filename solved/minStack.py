# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
 

# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack:
    # initiate the stack with two arrays
    def __init__(self):
        # this array is the functional stack
        self.arr = []
        # this array tracks the minimum value
        self.min = []
    # method for adding a value to the stack
    def push(self, x):
        # add the value to the stack
        self.arr.append(x)
        # if the minimum value array is empty, add the value to the minimum value array
        if len(self.min) == 0:
            self.min.append(x)
        # if the minimum value array is not empty and if the last value in the minimum value array is more than, or equal to, the value being added to the stack, then add the value to the minimum value array
        elif self.min[-1] >= x:
            self.min.append(x)
    # method for removing a value from the stack
    def pop(self):
        # if the stack has values
        if len(self.arr) > 0:
            # remove the last value from the stack and store it in a variable
            x = self.arr.pop()
            # if the stored value is equal to the last value in the minimum value array, remove the last value from the minimum value array
            if x == self.min[-1]:
                self.min.pop()
    # method for retrieving the last-added value from the stack
    def top(self):
        # if the stack has values
        if len(self.arr) > 0:
            # initiate a variable with a value of the last value from the stack and return the variable
            x = self.arr[-1]
            return x
    # method for retrieving the minimum value from the stack
    def getMin(self):
        # if the minimum value array has values
        if len(self.min) > 0:
            # initiate a variable with the value of the last value from the minimum value array and return the variable
            x = self.min[-1]
            return x

# takes a long time
class myMinStack:
    def __init__(self):
        self.arr = []
    def push(self, x):
        self.arr.append(x)
    def pop(self):
        if len(self.arr) > 0:
            self.arr.pop()
    def top(self):
        if len(self.arr) > 0:
            x = self.arr[-1]
            return x
    def getMin(self):
        if len(self.arr) > 0:
            x = min(self.arr)
            return x

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
param_1 = obj.getMin()
obj.pop()
param_2 = obj.top()
param_3 = obj.getMin()
print(param_1)
print(param_2)
print(param_3)
