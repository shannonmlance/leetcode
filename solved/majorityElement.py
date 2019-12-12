# Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times. You may assume that the array is non-empty and the majority element always exists in the array.

# Example 1:
# Input: [3,2,3]
# Output: 3

# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums):
        # initiate an empty dictionary
        d = {}
        # iterate through the array
        for i in range(len(nums)):
            # if the current value is a key in the dictionary
            if nums[i] in d:
                # increment the value associated with that key
                d[nums[i]] += 1
            # if the current value is not a key in the dictionary
            else:
                # add the current value as a key in the dictionary, using 1 as the key's value
                d[nums[i]] = 1
        # initiate a variable for storing the value that appears most in the array
        # initialize it with the first number from the array
        # initialize it as an array, setting the first index as the key from the dictionary and the second index as the value associated with that key
        m = [nums[0], d[nums[0]]]
        # iterate through the dictionary
        for k in d:
            # if the value associate with the current key is more than the value stored in the appears-most array, set the current key and value as the appears-most key and value
            if d[k] > m[1]:
                m = [k, d[k]]
        # return the value that appears the most
        return m[0]

nums = [2,2,1,1,1,2,2]
s = Solution()
a = s.majorityElement(nums)
print(a)