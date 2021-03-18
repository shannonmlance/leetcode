# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Follow up:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5

class Solution:
    def rotate(self, nums, k):
        # quick exit for if the given array contains only one value
        if len(nums) == 1:
            return nums
        # repeat as long as the given rotation number is bigger than the length of the given array
        while k >= len(nums):
            # subtract the length of the given array from the given rotation number
            k -= len(nums)
        # repeat as many times as the rotation number
        for i in range(k):
            # remove the last value from the given array and store it in a variable
            x = nums.pop()
            # insert the value stored in the variable at the beginning of the given array
            nums.insert(0, x)
        return

nums = [1,2,3,4,5,6,7]
k = 4
s = Solution()
s.rotate(nums, k)
print(nums)
