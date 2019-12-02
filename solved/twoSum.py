# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        # create a dictionary using the values of the array as the dictionary keys, and the indices of the array as the dictionary values
        d = dict([(nums[i],i) for i in range(len(nums))])
        # iterate through the array
        for n in range(len(nums)):
            # find the difference between the target number and the integer in the array
            dif = target - nums[n]
            # find the difference as a key in the dictionary, be careful that the dictionary's value is not the same as the array's indice (can happen when the difference is half of the target number, but there are not two halves in the array)
            if dif in d and d[dif] != n:
                # if found, return the two indices of the numbers that add up to the target number
                return (n,d[dif])
        # just in case there is no solution, even though the problem allows for the assumption that there is always one solution
        return ("No solution available")

# initilize a test case
s = Solution()
nums = [7,2,7,15]
target = 14
a = s.twoSum(nums,target)
print(a)

# create a dictionary that stores the indices as the keys and the integers as the values
# iterate through the array, attempting to find the target minus the integer as a key in the dictionary
# return the indice of the integer and the value of the key
# watch out for arrays that involve duplicates, such as [3,3,7,2], target 6