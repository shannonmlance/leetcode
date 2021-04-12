# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
# The maximum number of consecutive 1s is 3.

# Note:
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxConsecutiveOnes = 0
        slowRunner = fastRunner = 0
        while fastRunner < len(nums):
            if nums[fastRunner] == 1:
                fastRunner += 1
            else:
                consecutiveOnes = fastRunner - slowRunner
                if consecutiveOnes > maxConsecutiveOnes:
                    maxConsecutiveOnes = consecutiveOnes
                fastRunner += 1
                slowRunner = fastRunner
        if nums[fastRunner - 1] == 1:
            consecutiveOnes = fastRunner - slowRunner
            if consecutiveOnes > maxConsecutiveOnes:
                maxConsecutiveOnes = consecutiveOnes
        return maxConsecutiveOnes

nums = [1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1]
s = Solution()
a = s.findMaxConsecutiveOnes(nums)
print(a)
