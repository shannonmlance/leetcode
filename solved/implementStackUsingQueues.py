# Implement the following operations of a stack using queues.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.

# Example:
# MyStack stack = new MyStack();
# stack.push(1);
# stack.push(2);  
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false

# Notes:
# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

class MyOneQueueStack:
    # Initialize your data structure here.
    def __init__(self):
        # initialize one array, which will be used as a queue
        self.queue = []
    # Push element x onto stack.
    def push(self, x):
        # add the new value to the end of the queue
        self.queue.append(x)
        # loop through the queue, except for the last value (the newly added value)
        for i in range(len(self.queue)-1):
            # temp = self.queue.pop(0)
            # self.queue.append(temp)
            # remove the first value from the queue and add it to the back
            # this rotates the values so that they represent stack-order
            self.queue.append(self.queue.pop(0))
    # Removes the element on top of the stack and returns that element.
    def pop(self):
        # return the first value in the queue
        return self.queue.pop(0)
    # Get the top element.
    def top(self):
        # remove the first value in the queue and store it in a variable
        x = self.queue.pop(0)
        # add the stored value back into the queue, using the push method to maintain proper queue/stack order
        self.push(x)
        # return the stored value
        return x
    # Returns whether the stack is empty.
    def empty(self):
        # if the length of the queue is equal to zero, then the queue is empty
        if len(self.queue) == 0:
            return True
        # if the length of the queue is not equal to zero, then the queue is not empty
        return False

class MyTwoQueueStack:
    # Initialize your data structure here.
    def __init__(self):
        # initialize two arrays which will be used as queues
        self.q1 = []
        self.q2 = []
        # initialize a counter for quick isEmpty reference
        self.count = 0
    # Push element x onto stack.
    def push(self, x):
        # increment the counter
        self.count += 1
        # if there are values in queue one, add the new value to queue one
        if len(self.q1) > 0:
            self.q1.append(x)
        # if there are no values in queue one, add the new value to queue two
        else:
            self.q2.append(x)
        return
    # Removes the element on top of the stack and returns that element.
    def pop(self):
        # decrement the counter
        self.count -= 1
        # if there are values in queue one
        if len(self.q1) > 0:
            # loop through queue one, except for the last value
            for i in range(len(self.q1)-1):
                # remove the first value from queue one and store it in a variable
                x = self.q1.pop(0)
                # put the stored value at the end of queue two
                self.q2.append(x)
            # remove the last value from queue one and store it in a variable
            x = self.q1.pop()
        # if there are no values in queue one
        else:
            # loop through queue two, except for the last value
            for i in range(len(self.q2)-1):
                # remove the first value from queue two and store it in a variable
                x = self.q2.pop(0)
                # put the stored value at the end of queue one
                self.q1.append(x)
            # remove the last value from queue two and store it in a variable
            x = self.q2.pop()
        # return the final stored value
        return x
    # Get the top element.
    def top(self):
        # if there are values in queue one
        if len(self.q1) > 0:
            # loop through queue one
            for i in range(len(self.q1)):
                # remove the first value from queue one and store it in a variable
                x = self.q1.pop(0)
                # put the stored value at the end of queue two
                self.q2.append(x)
        # if there are no values in queue one
        else:
            # loop through queue two
            for i in range(len(self.q2)):
                # remove the first value from queue two and store it in a variable
                x = self.q2.pop(0)
                # put the stored value at the end of queue one
                self.q1.append(x)
        # return the final stored and moved value
        return x
    # Returns whether the stack is empty.
    def empty(self):
        # if the counter is equal to zero, return true, as the stack is empty
        if self.count == 0:
            return True
        # if the counter is not equal to zero, return false, as the stack is not empty
        return False

# Your MyStack object will be instantiated and called as such:
obj = MyOneQueueStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
a = obj.top()  # should return 4
b = obj.pop()  # should return 4
c = obj.pop()  # should return 3
d = obj.top()  # should return 2
obj.push(5)
e = obj.top()  # should return 5
f = obj.empty()  # should return False
g = obj.pop()  # should return 5
h = obj.pop()  # should return 2
i = obj.pop()  # should return 1
j = obj.empty()  # should return True

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
print(obj.queue)
# print(obj.q2)