# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:
# Input: [1,2,3,1]
# Output: True

# Example 2:
# Input: [1,2,3,4]
# Output: False

# Example 3:
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: True

# allows for early exit
class Solution:
    def containsDuplicate(self, nums):
        # initiate an empty set
        s = set()
        # iterate through the given array
        for i in nums:
            # if number is already in the set, then there are duplicates
            if i in s:
                return True
            # if the number is not already in the set, add it to the set
            s.add(i)
        # if all numbers in the set are unique, then there are no duplicates
        return False

class mySolution:
    def containsDuplicate(self, nums):
        # set contains only unique numbers
        # if the length of the set of the given array and the length of the given array are not equal, then there are duplicates
        return len(set(nums)) != len(nums)

nums = [1,1,2,3,4,5]
s = Solution()
a = s.containsDuplicate(nums)
print(a)
