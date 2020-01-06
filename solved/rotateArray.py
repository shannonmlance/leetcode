# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Note:
# Try to come up with as many solutions as you can. There are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

class Solution:
    def rotate(self, nums, k):
        # prevents from rotating entire array to same position (or rotating more than one full loop)
        k = k % len(nums)
        # reverse the entire array
        nums.reverse()
        # reverse the first half of the array, from the beginning up to k
        self.rev(nums, 0, k-1)
        # reverse the second half of the array, from k to the end
        self.rev(nums, k, len(nums)-1)
    # helper method for reversing part of an array
    def rev(self, nums, start, end):
        # continue until the entire section has been reversed
        while start < end:
            # store the first value in a variable
            temp = nums[start]
            # change the first value to equal the end value
            nums[start] = nums[end]
            # change the end value to equal the variable
            nums[end] = temp
            # increment the beginning
            start += 1
            # decrement the ending
            end -= 1

# takes really long
class oneSolution:
    def rotate(self, nums, k):
        for i in range(k):
            num = nums.pop()
            nums.insert(0, num)
        return

nums = [1,2,3,4,5,6,7]
s = Solution()
s.rotate(nums, 22)
print("*"*20)
print(nums)