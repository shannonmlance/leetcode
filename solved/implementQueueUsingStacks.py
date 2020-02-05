# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.

# Example:
# MyQueue queue = new MyQueue();
# queue.push(1);
# queue.push(2);  
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false

# Notes:
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

# push is always O(1)
# depending on order of operations, pop could have times as bad as O(n), but will usually be O(1) (amortized)
# peek is O(1)
class MyQueue:
    # initialize your data structure here
    def __init__(self):
        # initiate the queue using two empty stacks
        self.stackA = []
        self.stackB = []
        # initiate a count variable to easily track if the queue is empty
        self.count = 0
        # innitiate a front variable to easily access for peek
        self.front = 0
    # push element x to the back of the queue
    def push(self, x):
        # if stack A is empty, set the front variable to the given value
        if len(self.stackA) == 0:
            self.front = x
        # add the given value to the end of stack A
        self.stackA.append(x)
        # increment the count variable
        self.count += 1
    # removes the element from in front of queue and returns that element
    def pop(self):
        # if stack B is empty
        if len(self.stackB) == 0:
            # as long as stack A is not empty
            while len(self.stackA) > 0:
                # remove the last value from stack A and add it to the end of stack B
                self.stackB.append(self.stackA.pop())
        # decrement the count variable
        self.count -= 1
        # remove and return the last value from stack B
        return self.stackB.pop()
    # get the front element
    def peek(self):
        # if stack B is empty, return the front variable from stack A
        if len(self.stackB) == 0:
            return self.front
        # if stack B is not empty, remove the last value from stack B and store it in a variable
        x = self.stackB.pop()
        # add the stored value back to the end of stack B, since we didn't want to remove it, just view it
        self.stackB.append(x)
        # return the stored value
        return x
    # returns whether the queue is empty
    def empty(self):
        # return the boolean of whether the count variable is equal to zero
        return self.count == 0

# depending on order of operations, push and pop could have times as bad as O(n) or as good as O(1)
class firstMyQueue:
    # initialize your data structure here
    def __init__(self):
        # initialize the queue with two empty stacks
        self.stackA = []
        self.stackB = []
        # initialize a count variable to easily track if the queue is empty
        self.count = 0
    # push element x to the back of queue
    def push(self, x):
        # as long as stack B is not empty
        while len(self.stackB) > 0:
            # remove the last value from stack B and add it to the end of stack A
            v = self.stackB.pop()
            self.stackA.append(v)
        # add the given value to the end of stack A
        self.stackA.append(x)
        # increment the count variable
        self.count += 1
    # removes the element from in front of queue and returns that element
    def pop(self):
        # as long as stack A is not empty
        while len(self.stackA) > 0:
            # remove the last value from stack A and add it to the end of stack B
            v = self.stackA.pop()
            self.stackB.append(v)
        # remove the last value from stack B and store it in a variable
        x = self.stackB.pop()
        # decrement the count variable
        self.count -= 1
        # return the stored value
        return x
    # get the front element
    def peek(self):
        # as long as stack A is not empty
        while len(self.stackA) > 0:
            # remove the last value from stack A and add it to the end of stack B
            v = self.stackA.pop()
            self.stackB.append(v)
        # remove the last value from stack B and store it in a variable
        x = self.stackB.pop()
        # add the stored value back to the end of stack B, since we didn't want to remove it, just view it
        self.stackB.append(x)
        # return the stored value
        return x
    # returns whether the queue is empty
    def empty(self):
        # return the boolean of whether the count variable is equal to zero
        return self.count == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
z = obj.empty() # returns True
obj.push(1)
obj.push(2)
a = obj.peek() # returns 1
obj.push(3)
obj.push(4)
b = obj.peek() # returns 1
c = obj.pop()  # returns 1
d = obj.peek() # returns 2
e = obj.empty() # returns False
obj.push(5)
f = obj.peek() # returns 2
g = obj.pop()  # returns 2
h = obj.pop()  # returns 3
i = obj.pop()  # returns 4
obj.push(6)
j = obj.empty() # returns False
k = obj.pop()  # returns 5
l = obj.pop()  # returns 6
m = obj.empty() # returns True
print(z)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)