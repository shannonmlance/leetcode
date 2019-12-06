# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:
# Input: [2,2,1]
# Output: 1

# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

# cool way to find this using bitwise operators
class Solution:
    def singleNumber(self, nums):
        # loop through the list
        for i in range(1, len(nums)):
            # set the current value equal to the bitwise value of the exclusive or between the current value and the previous value
            # exclusive or works like this:
                # when comparing bitwise numbers, if one but not both of the numbers are 1, return 1. otherwise, return 0
                # 4^2 = 100^10 = 110 = 6
                # 15^3 = 1111^11 = 1100 = 12
                # 9^5 = 1001^101 = 1100 = 12
            # when two values that are the same are encountered, they cancel themselves out. Thus, at the end of the array, the final value is equal to the unmatched value
            nums[i] = nums[i]^nums[i-1]
        # return the last value in the array
        return nums[-1]

# fine solution
class myGoodSolution:
    def singleNumber(self, nums):
        # sort the list
        nums.sort()
        # initiate a pointer
        i = 0
        # loop through the list
        while i < len(nums)-1:
            # if the current value is the same as the one directly before it
            if nums[i] == nums[i+1]:
                # skip ahead
                i += 2
            # if the current value is not the same as the one directly before it, the unmatched number has been located
            else:
                break
        # return the unmatched number
        return nums[i]

# exceeds timelimit
class mySolution:
    def singleNumber(self, nums):
        i = 1
        while i < len(nums):
            if nums[0] == nums[i]:
                nums.pop(i)
                nums.pop(0)
                i = 1
            else:
                i += 1
        return nums[0]

nums = [10,9,12,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,10,11,11]
s = Solution()
a = s.singleNumber(nums)
print(a)
