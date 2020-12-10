# In a given integer array nums, there is always exactly one largest element. Find whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, otherwise return -1.

# Example 1:
# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the array x, 6 is more than twice as big as x. The index of value 6 is 1, so we return 1.

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

# Note:
# nums will have a length in the range [1, 50].
# Every nums[i] will be an integer in the range [0, 99].

# using max variables
class Solution:
    def dominantIndex(self, nums):
        # initiate variables for the largest value and second largest value, with corresponding indexes
        largestValue = nums[0]
        secondValue = 0
        largestIndex = 0
        secondIndex = -1
        # perform the following for each value in the given array, except the first
        for i in range(1, len(nums)):
            # if the current value is larger than the current largest value
            if nums[i] > largestValue:
                # set the largest value as the second largest value
                secondValue = largestValue
                # set the current value as the largest value
                largestValue = nums[i]
                # set the largest value's index as the second largest value's index
                secondIndex = largestIndex
                # set the current value's index as the largest value's index
                largestIndex = i
            # if the current value is not larger than the current largest value, and the current value is larger than the current second largest value
            elif nums[i] > secondValue:
                # set the current value as the second largest value
                secondValue = nums[i]
                # set the current value's index as the second largest value's index
                secondIndex = i
        # if the largest value is equal to, or more than, twice the second largest value
        if largestValue >= secondValue * 2:
            # return the largest value's index
            return largestIndex
        # if the largest value is not equal to, or more than, twice the second largest value, return an index of negative one
        return -1

# using sorting function
class firstSolution:
    def dominantIndex(self, nums):
        # if the given array contains only one value, that value is, by default, twice all others
        if len(nums) == 1:
            return 0
        # sort the array, in descending order
        s = sorted(nums,reverse=True)
        # if the first value in the sorted array is equal to, or more than, double of the second value, find and return the index of the first value of the sorted array in the given array
        if s[0] >= s[1] * 2:
            return nums.index(s[0])
        # if the first value in the sorted array is not equal to, or more than, double of the second value, return an index of negative one
        return -1

nums = [1,2,3,49,5,6,7,8,9]
s = Solution()
a = s.dominantIndex(nums)
print(a)
