# Given an array of integers nums, write a method that returns the "pivot" index of this array. We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation: The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3. Also, 3 is the first index where this occurs.

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation: There is no index that satisfies the conditions in the problem statement.

# Constraints:
# The length of nums will be in the range [0, 10000].
# Each element nums[i] will be an integer in the range [-1000, 1000].

class Solution:
    def pivotIndex(self, nums):
        # if the array is empty, then there is no left and right of the pivot index
        if len(nums) < 1:
            return -1
        # initialize the pivot at index 0
        pivot = 0
        # initialize the sum of the left of the pivot as nothing (if the pivot is at index 0, there are no values to the left)
        left = 0
        # initialize the sum of the right of the pivot as the sum of the entire array, minus the value at the pivot index
        right = sum(nums) - nums[pivot]
        # perform this loop as long as the pivot is less than the length of the array, minus one, and as long as the left and right variables do not equal the same value
        while pivot < len(nums)-1 and left != right:
            # move the pivot index to the right
            # add the current pivot index's value to the left variable
            left += nums[pivot]
            # subtract the next pivot index's value from the right variable
            right -= nums[pivot+1]
            # increment the pivot index
            pivot += 1
        # if the left and right variable equal the same value, then return the current pivot index
        if left == right:
            return pivot
        # else, return -1 as there is no valid pivot index
        return -1

nums = [-1,-1,-1,0,1,1]
s = Solution()
a = s.pivotIndex(nums)
print(a)