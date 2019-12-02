# Given two sorted integer arrays, nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

# Example:
# Input:
    # nums1 = [1,2,3,0,0,0], m = 3
    # nums2 = [2,5,6],       n = 3
# Output: [1,2,2,3,5,6]

# faster and less code, easier to read
class Solution:
    def merge(self, nums1, m, nums2, n):
        # set pointer variables for traversing the sorted array portions of nums1 and nums2
        i = m - 1
        j = n - 1
        # set pointer variable for tracking the entirety of nums1, from the right to the left
        idx = len(nums1) - 1
        # loop through the sorted portions of the two arrays, starting at the right, until one of them runs out of indices
        while i >= 0 and j >= 0:
            # if the value in nums1 is less than the value in nums2
            if nums1[i] < nums2[j]:
                # put the value of nums2 at the end of the unsorted portion of nums1
                nums1[idx] = nums2[j]
                # decrement the nums2 pointer
                j -= 1
                # decrement the placement pointer
                idx -= 1
            # if the value in nums1 is not less than the value in nums2
            else:
                # put the value of nums1 at the end of the unsorted portion of nums1
                nums1[idx] = nums1[i]
                # decrement the nums1 pointer
                i -= 1
                # decrement the placement pointer
                idx -= 1
        # loop through the remainder of values in nums2
        while j >= 0:
            # put the value of nums2 at the end of the unsorted portion of nums1
            nums1[idx] = nums2[j]
            # decrement the nums2 pointer
            j -= 1
            # decrement the placement pointer
            idx -= 1

class mySolution:
    def merge(self, nums1, m, nums2, n):
        # if nums2 is an empty array, then nums1 does not need to be adjusted
        if n == 0:
            return
        # initialize pointers for nums1 and nums2
        i = 0
        j = 0
        # loop through both arrays until one of them is done
        while i < m-1 and j < n:
            # if the value at nums2 is less than the value at nums1
            if nums2[j] < nums1[i]:
                # remove the placeholder at the end of nums1
                nums1.pop()
                # insert the value at nums2 before the value at nums1
                nums1.insert(i, nums2[j])
                # increment the length of the sorted portion of nums1
                m += 1
                # increment the nums2 pointer
                j += 1
            # if the value at nums2 is greater than the value at nums1 and less than the next value at nums1
            if (nums1[i] <= nums2[j] <= nums1[i+1]):
                # remove the placeholder at the end of nums1
                nums1.pop()
                # insert the value at nums2 after the value at nums1
                nums1.insert(i+1, nums2[j])
                # increment the length of the sorted portion of nums1
                m += 1
                # increment the nums1 pointer
                i += 1
                # increment the nums2 pointer
                j += 1
            # if the value at nums2 is greater than the next value at nums1
            else:
                # increment the nums1 pointer
                i += 1
        # loop through both arrays until one of them is done
        while i < m and j < n:
            # if the value at nums2 is less than the value at nums1
            if nums2[j] < nums1[i]:
                # remove the placeholder at the end of nums1
                nums1.pop()
                # insert the value at nums2 before the value at nums1
                nums1.insert(i, nums2[j])
                # increment the length of the sorted portion of nums1
                m += 1
                # increment the nums2 pointer
                j += 1
            # if the value at nums2 is not less than the value at nums1
            else:
                # increment the nums1 pointer
                i += 1
        # loop through remaining placeholders in nums1
        while m < len(nums1):
            # remove all of them
            nums1.pop()
        # loop through the remaining values in nums2
        while j < n:
            # add them to the end of nums1
            nums1.append(nums2[j])
            # increment the nums2 pointer
            j += 1
        return

nums1 = [1,2,3,4,5,0,0,0,0]
m = 5
nums2 = [1,4,9,9]
n = 4
s = Solution()
s.merge(nums1,m,nums2,n)
print(nums1)
