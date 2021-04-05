# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1

# Follow up: Could you minimize the total number of operations done?

# long solution
class mySolution:
    def swap(self, nums, i, j):
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp
    def moveZeroes(self, nums):
        i = 0
        j = len(nums) - 1
        frontSize = 0
        backSize = 0
        while i < j:
            if nums[j] == 0:
                j -= 1
            else:
                self.swap(nums, i, j)
                j -=1
                i += 1
                frontSize += 1
        if nums[i] != 0:
            frontSize += 1
        i += 1
        j = len(nums) - 1
        while i < j:
            if nums[i] == 0:
                i += 1
            else:
                self.swap(nums, i, j)
                j -= 1
                i += 1
                backSize += 1
        if nums[j] != 0:
            backSize += 1
        i = frontSize
        j = len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            j -= 1
            i += 1
        i = 0
        j = frontSize + backSize - 1
        while i < j:
            self.swap(nums, i, j)
            j -= 1
            i += 1
        return

# optimized solution
class Solution:
    # helper method for swapping two values in an array
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    # main method
    def moveZeroes(self, nums):
        # initiate two runners at the beginnig of the given array
        slow = 0
        fast = 0
        # loop through the given array with the fast runner
        while fast < len(nums):
            # if the value of the fast runner is not zero
            if nums[fast] != 0:
                # swap the value of the fast runner with the value of the slow runner
                self.swap(nums, slow, fast)
                # increment the slow runner
                slow += 1
            # increment the fast runner
            fast += 1
        return

nums = [0,1,2,3,0,0,0,0,0,1,0,0,0,0,2,0,0,0,3,0,0]
s = Solution()
s.moveZeroes(nums)
print(nums)
