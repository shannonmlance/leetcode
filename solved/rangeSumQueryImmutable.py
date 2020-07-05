# Given an integer array, nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3

# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.

class NumArray:
    # initiate the class
    def __init__(self, nums):
        # assign the given array to a variable within the function
        self.nums = nums
        # initiate a variable for storing the current sum
        sum = 0
        # I am going to change the stored array so the each value becomes the sum of all previous values. This way, when calling the method sumRange, no looping is necessary.
        # loop through the given array
        for i in range(len(nums)):
            # initiate a variable to store the current value in the array
            temp = nums[i]
            # change the current value in the function's array to equal the current sum
            self.nums[i] = sum
            # add the temp variable to the sum variable
            sum += temp
        # if the given array is empty, set the function's array to have a value of zero. This prevents out of range errors when calling the method
        if len(nums) == 0:
            self.nums = [0]
        # add the final sum to the end of the array
        self.nums.append(sum)
    def sumRange(self, i, j):
        # since the question asks for both start and end indexes to be inclusive, return the start value of the array (the summation of all values up to the start index) subtracted from the end value plus one of the array (the summation of all values up to and including the end index)
        return self.nums[j+1] - self.nums[i]

# time limit exceeded
class myNumArray:
    def __init__(self, nums):
        self.nums = nums
    def sumRange(self, i, j):
        if i == j:
            return self.nums[i]
        mid = (j - i)//2 + i
        left = self.sumRange(i, mid)
        right = self.sumRange(mid + 1, j)
        return left + right



nums = []
# Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
param_1 = obj.sumRange(0,0)
print(param_1)