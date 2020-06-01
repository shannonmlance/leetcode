# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:
# Input: [3,0,1]
# Output: 2

# Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

class Solution:
    def missingNumber(self, nums):
        # multiply the length of the array by the length of the array plus one
        # divide the product by 2
        # subtract the quotient by the sum of the numbers in the array
        return (len(nums) * (len(nums) + 1)//2) - sum(nums)

# on leetcode, performs just as well as the above solution, but should perform worse, since it has a loop
class mySolution:
    def missingNumber(self, nums):
        # initiate a counter at zero
        c = 0
        # run a loop as long as the array (inclusive)
        for i in range(len(nums)+1):
            # add the value of the iterator to the counter
            c += i
        # subtract the sum of the numbers in the array from the counter
        return c - sum(nums)

nums = [0,2,4,6,8,10,12,14,13,1,9,7,5,3]
s = Solution()
a = s.missingNumber(nums)
print(a)
