# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array.

# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6], 2
# Output: 1

# Example 3:
# Input: [1,3,5,6], 7
# Output: 4

# Example 4:
# Input: [1,3,5,6], 0
# Output: 0

class Solution:
    def searchInsert(self, nums, target):
        # if the array is empty, the target would be inserted at the beginning, so return index 0
        if len(nums) == 0:
            return 0
        # iterate through the array
        for i in range(len(nums)):
            # if the target is less than the number in the array, then the target would be inserted at this index, so return the current value of the iterator
            # if the target is equal to the number in the array, then the target has been located, so return the current value of the iterator
            if target <= nums[i]:
                return i
        # if the entire array has been searched and the target number has not been found, and the target number is bigger than all the numbers in the array, then the target would be inserted at the end of the array, so return the length of the array
        return len(nums)

nums = []
target = 3
s = Solution()
a = s.searchInsert(nums, target)
print(a)