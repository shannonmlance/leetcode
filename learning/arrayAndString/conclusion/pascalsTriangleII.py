# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]

# Constraints:
# 0 <= rowIndex <= 33

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

# Beginning rows of Pascal's Triangle are as follows:
# 0. [1]
# 1. [1,1]
# 2. [1,2,1]
# 3. [1,3,3,1]
# 4. [1,4,6,4,1]
# 5. [1,5,10,10,5,1]
# 6. [1,6,15,20,15,6,1]
# 7. [1,7,21,35,35,21,7,1]
# 8. [1,8,28,56,70,56,28,8,1]
# 9. [1,9,36,84,126,126,84,36,9,1]
# 10.[1,10,45,120,210,252,210,120,45,10,1]

class Solution:
    def getRow(self, rowIndex):
        # initiate an array where rowIndex = 0
        arr = [1]
        # loop as many times as rowIndex
        for i in range(rowIndex):
            # loop through the current answer array, starting with the second value
            for j in range(1,len(arr)):
                # change the previous value to the sum of the current value plus the previous value
                arr[j - 1] = arr[j - 1] + arr[j]
            # insert a 1 at the beginning of the answer array
            arr.insert(0, 1)
        return arr

rowIndex = 10
s = Solution()
a = s.getRow(rowIndex)
print(a)