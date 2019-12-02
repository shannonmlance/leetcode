# Given a non-negative integer, numRows, generate the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:
# Input: 5
# Output:
# [
#         [1],
#        [1,1],
#       [1,2,1],
#      [1,3,3,1],
#     [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows):
        # initiate an empty array to store the requested levels of the triangle
        arr = []
        # if no rows are requested, then there's nothing to return
        if numRows == 0:
            return
        # for each row requested, run the helper method and add the result into the array
        for i in range(1, numRows + 1):
            arr.append(self.pascal(i))
        return arr
    # helper function for return a specific row of the triangle
    def pascal(self, numRows):
        # base case
        # if the requested row is the first row, return the first row of pascals triangle
        if numRows == 1:
            return [1]
        # if the requested row is not the first row
        else:
            # recursively call the helper method, asking for the previous row
            prevArr = self.pascal(numRows - 1)
            # initiate an array to store the requested row's values, and start it with the number 1
            currentArr = [1]
            # add each number in the previous row, except for the final number, to the next number and place the sum in the requested row's array
            for i in range(len(prevArr) - 1):
                currentArr.append(prevArr[i] + prevArr[i+1])
            # add a final 1 to the end of the requested row's array and return the array
            currentArr.append(1)
            return currentArr

numRows = 6
s = Solution()
a = s.generate(numRows)
print(a)