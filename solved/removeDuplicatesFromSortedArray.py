# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Given nums = [1,1,2], your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

# Example 2:
# Given nums = [0,0,1,1,1,2,2,3,3,4], your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

# Internally you can think of this:
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

class Solution:
    def removeDuplicates(self, nums):
        # if there is only one number, or if there are no numbers, in the array, then there can be no duplicates
        if len(nums) < 2:
            # return the length of the array
            return len(nums)
        # set a counter for unique numbers
        int = 0
        # as long as the counter is one less than the length of the input array, iterate through the array
        while int < len(nums) - 1:
            # if the current number in the array is the same as the next number in the array
            if nums[int] == nums[int+1]:
                # remove the number from the array
                nums.pop(int)
                # do not increment the counter, as numbers in the array have shifted to the left and the same indice needs to be evaluated against its neighbor
            # if the current number in the array is not the same as the next number in the array
            else:
                # then the current number is unique and should be left in the array
                # increment the counter to evaluate the next number
                int += 1
        # once all numbers in the array have been evaluated against their neighbors, and all duplicates have been removed, return the length of the array
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
a = s.removeDuplicates(nums)
print(a)