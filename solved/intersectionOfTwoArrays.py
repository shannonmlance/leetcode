# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]

# Note:
# Each element in the result must be unique.
# The result can be in any order.

class Solution:
    def intersection(self, nums1, nums2):
        # get only unique values out of both lists
        s1 = set(nums1)
        s2 = set(nums2)
        # initiate an empty array
        s3 = []
        # loop  through first set
        for i in s1:
            # if the value is also in the second set
            if i in s2:
                # add the value to the empty array
                s3.append(i)
        return s3

nums1 = [1,2,3,4,5,6,7,8,9]
nums2 = [9,1,8,2]
s = Solution()
a = s.intersection(nums1, nums2)
print(a)