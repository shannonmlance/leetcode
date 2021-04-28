# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.

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

class Solution:
    def moveZeroes(self, nums):
        slow = 0
        while slow < len(nums) and nums[slow] != 0:
            slow += 1
        fast = slow + 1
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return

nums = [0,0,0,1,2,3,0,0,0,4,5,6,0,0,0,7,8,9]
s = Solution()
s.moveZeroes(nums)
print(nums)