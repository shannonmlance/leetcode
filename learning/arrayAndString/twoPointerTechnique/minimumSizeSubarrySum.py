# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

class Solution:
    def minSubArrayLen(self, s, nums):
        # if the given array is empty, return 0
        if  len(nums) == 0:
            return 0
        # initiate a counter for the minimal length of a subarray, and set its value for more than the length of the given array
        count = len(nums) + 1
        # initiate a pointer and a runner, both at the beginning of the array
        i = j = 0
        # initiate a variable for the sum of the subarray, with a variable equal to the value of the first index
        tempSum = nums[i]
        # loop through the given array
        while i < len(nums):
            # if the pointer and runner are at the same index
            if i == j:
                # and if the value at that index is equal to, or more than, the given target number
                if nums[i] >= s:
                    # return 1
                    return 1
            # loop through the array with the runner, as long as the sum variable is less than the given target
            while j < len(nums) - 1 and tempSum < s:
                # increment the runner
                j += 1
                # add the runner's value to the sum variable
                tempSum += nums[j]
            # if the sum variable is equal to, or more than, the given target
            # and if the difference between the runner and the pointer is less than the counter variable
            if tempSum >= s and j - i < count:
                # set the counter variable equal to the difference between the runner and the pointer
                count = j - i
            # loop through the array with the pointer, as long as as the pointer doesn't meet the runner, and as long as the sum variable is equal to, or greater than, the target
            while i < j and tempSum >= s:
                # subtract the pointer's value from the sum variable
                tempSum -= nums[i]
                # increment the pointer
                i += 1
            # if the difference between the runner and the pointer, plus one, is less than the counter variable
            if j - i + 1 < count:
                # set the counter variable equal to the difference between the runner and the pointer, plus one
                count = j - i + 1
            # if the runner is at the end of the array
            if j == len(nums) - 1:
                # and if the counter variable, plus one, is more than the length of the array, retun 0
                if count + 1 > len(nums):
                    return 0
                # else, return the counter variable, plus one
                return count + 1

s = 63
nums = [132]
sol = Solution()
a = sol.minSubArrayLen(s, nums)
print(a)