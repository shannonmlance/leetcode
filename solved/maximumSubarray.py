# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums):
        # if the input array is empty, there is no maximum subarray
        if len(nums) == 0:
            return None
        # if the input array contains only one value, there is no subarray, so the sole value can be returned as the max
        if len(nums) == 1:
            return nums[0]
        # iterate through the input array, starting at the second index
        for i in range(1, len(nums)):
            # if the previous index is greater than 0, it should be included in the subarray
            if nums[i-1] > 0:
                # add the previous index's value to the current index's value to keep a running total of the subarray's value
                nums[i] += nums[i-1]
        # from the modified input array, return the maximum value
        return max(nums)

nums = []
s = Solution()
a = s.maxSubArray(nums)
print(a)