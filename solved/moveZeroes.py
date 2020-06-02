# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums):
        # add all the values in nums array and store in a variable
        s = sum(nums)
        # initiate a count variable at zero
        c = 0
        # initiate an iterator variable at zero
        i = 0
        # as long as the count variable does not equal the sum of the array
        # do it this way to avoid iterating through zeroes at the end of the array
        while c != s:
            # if the current number is zero
            if nums[i] == 0:
                # remove the zero and store it in a variable
                x = nums.pop(i)
                # append the zero to the end
                nums.append(x)
            # if the current number is not zero
            else:
                # add the current number to the count variable
                c += nums[i]
                # increment the iterator
                i += 1
        return

nums = [1,0,0,0,0,6,3,9,6,0,0,2,7,0,0,5,3,8,0,0,4,7,0,0,0]
s = Solution()
s.moveZeroes(nums)
print("*"*10)
print(nums)