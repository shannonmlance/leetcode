# Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times. You may assume that the array is non-empty and the majority element always exists in the array.

# Example 1:
# Input: [3,2,3]
# Output: 3

# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2

# optimized solution
# runs in O(n) for time and O(1) for space
class Solution:
    def majorityElement(self, nums):
        # initiate a variable equal to the value stored at the first index of the given array
        ans = nums[0]
        # initiate a counter, starting at one since we already know there's at least one of the value stored in the above variable
        count = 1
        # iterate through the array, starting at the second index
        for i in range(1, len(nums)):
            # whenever the counter reaches zero
            if count == 0:
                # set the answer variable to the current value in the array
                ans = nums[i]
            # if the current value in the array is the same as the answer value, increment the counter
            if nums[i] == ans:
                count += 1
            # if the current value in the array is not the same as the answer value, decrement the counter
            if nums[i] != ans:
                count -= 1
        # return the final answer
        return ans

# works just fine
# runs in O(n) for both time and space
class mySolution:
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

nums = [7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
s = Solution()
a = s.majorityElement(nums)
print(a)