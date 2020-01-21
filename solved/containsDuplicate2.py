# Given an array of integers and an integer k, find out whether there are two distinct indices, i and j, in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: True

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: True

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: False

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        # initialize a dictionary
        d = {}
        # loop through the given array
        for i in range(len(nums)):
            # if the current value is in the dictionary
            if nums[i] in d:
                # and if the difference between the current index and the previous same value's index is less than, or equal to, k, then we have found a solution
                if i - d[nums[i]] <= k:
                    return True
            # either create or update the dictionary with a key of the current iteration's value and a value of the index
            d[nums[i]] = i
        # if loop completes, then an answer was not found
        return False

# probably will time out
class mySolution:
    def containsNearbyDuplicate(self, nums, k):
        # need a separate solution for if k is equal to or greater than the length of the given array
        if k >= len(nums):
            # loop through the entire given array
            for i in range(len(nums)):
                # for each iteration, loop through the rest of the given array
                for j in range(i+1, len(nums)):
                    # until you find two values that are equal
                    if nums[i] == nums[j]:
                        return True
        # if k is less tan the length of the given array
        else:
            # loop through the entire given array less the amount of k, to avoid out of range errors
            for i in range(len(nums)-k):
                # for each iteration, loop through the rest of the given array k number of times
                for j in range(i+1, k+i+1):
                    # until you find two values that are equal
                    if nums[i] == nums[j]:
                        return True
        return False

nums = [1,2,3,4,1,2,3,5,1,2,3,4]
k = 4
s = Solution()
a = s.containsNearbyDuplicate(nums, k)
print(a)
