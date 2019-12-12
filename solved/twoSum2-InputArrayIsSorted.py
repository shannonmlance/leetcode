# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number. The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

# Note:
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.

# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

# requires less memory
class Solution:
    def twoSum(self, numbers, target):
        # initiate two pointers, one at the beginning of the array and one at the end
        start = 0
        end = len(numbers) - 1
        # continue looping until the two pointers meet
        while start < end:
            # initiate a variable equal to the sum of the two pointers
            sum = numbers[start] + numbers[end]
            # if the sum of the two pointers is equal to the target number, then the two values have been found
            if sum == target:
                # return the indices (plus one since this is not zero-based) in order of smallest to largest
                return [start+1, end+1]
            # if the sum of the two pointers is less than the target number, then the lower pointer needs to be incremented
            elif sum < target:
                start += 1
            # if the sum of the two pointers is not less than or equal to the target number, then the upper pointer needs to be decremented
            else:
                end -= 1
        return

class mySolution:
    def twoSum(self, numbers, target):
        # initiate an empty dictionary
        d = {}
        # loop through the array
        for i in range(len(numbers)):
            # set a variable equal to the difference between the target number and the current value in the array
            comp = target - numbers[i]
            # if the variable equal to the difference between the target number and the current value in the array is a key in the dictionary, then the two values have been found
            if comp in d:
                # return the indices (plus one since this is not zero-based) in order of smallest to largest
                return [d[comp]+1, i+1]
            # if the variable equal to the difference between the target number and the current value in the array is not a key in the dictionary, add it to the dictionary using the variable as the key and the indice as the value
            else:
                d[numbers[i]] = i
        return

numbers = [2,7,11,15]
target = 17
s = Solution()
a = s.twoSum(numbers, target)
print(a)