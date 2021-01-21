# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Note:
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

import random

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # initiate an empty variable for storing the maximum number of consecutive ones
        maxConsecutive = 0
        # initiate a pointer and a runner, both set at the beginning of the given array
        i = j = 0
        # loop through the entire array
        while i < len(nums):
            # initiate a temporary counter of consecutive ones
            count = 0
            # loop through the array, as long as the current value is a one
            while j < len(nums) and nums[j] == 1:
                # increment the temporary counter
                count += 1
                # increment the runner
                j += 1
            # if the temporary counter is greater than the maximum counter
            if count > maxConsecutive:
                # set the maximum counter's value equal to the temporary counter
                maxConsecutive = count
            # increment the runner
            j += 1
            # move the pointer to the runner's place
            i = j
        return maxConsecutive
    # helper method for creating random arrays
    def createArray(self, num):
        # initiate an empty array
        arr = []
        # loop through the given number of times
        for i in range(num):
            # randomly pick a zero or a one
            x = random.randint(0,1)
            # add the random number to the array
            arr.append(x)
        return arr

s = Solution()
num = 0
nums = s.createArray(num)
print(nums)
a = s.findMaxConsecutiveOnes(nums)
print(a)