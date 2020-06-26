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
    def __init__(self, nums):
        self.nums = nums
        sum = 0
        for i in range(len(nums)):
            temp = nums[i]
            self.nums[i] = sum
            sum += temp
        if len(nums) == 0:
            self.nums = [0]
        self.nums.append(sum)
    def sumRange(self, i, j):
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