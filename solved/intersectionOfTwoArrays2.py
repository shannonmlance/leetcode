# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

class Solution:
    def intersect(self, nums1, nums2):
        # initiate an empty array
        nums3 = []
        # sort both given arrays
        nums1.sort()
        nums2.sort()
        # set markers for traversing both given arrays
        i = j = 0
        # loop as long as both arrays have value
        while i < len(nums1) and j < len(nums2):
            # if both values are equal
            if nums1[i] == nums2[j]:
                # add the value to the empty array
                nums3.append(nums1[i])
                # increment both markers
                i += 1
                j += 1
            # if the value of the first array is less than the value of the second array
            elif nums1[i] < nums2[j]:
                # increment the marker for the first array
                i += 1
            # if the value of the first array is more than the value of the second array
            elif nums1[i] > nums2[j]:
                # increment the marker for the second array
                j += 1
        return nums3

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
s = Solution()
a = s.intersect(nums1, nums2)
print(a)
