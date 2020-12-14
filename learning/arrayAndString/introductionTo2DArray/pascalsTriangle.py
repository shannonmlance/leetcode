# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution():
    def generate(self, numRows):
        # if the given integer is zero, return an empty array
        if numRows == 0:
            return []
        # initialize the first row in the triangle
        matrix = [[1]]
        # loop for adding rows
        for i in range(1, numRows):
            self.addRow(i, matrix)
        return matrix
    # helper function takes the current matrix and the next row to add
    def addRow(self, row, matrix):
        # initialize the next row
        matrix.append([])
        # add the starting 1 to the row
        matrix[row].append(1)
        # loop to add the remaining numbers to the row
        for i in range(1, len(matrix[row - 1])):
            # take the summation of the two numbers above the current number
            s = matrix[row-1][i-1] + matrix[row-1][i]
            # add that sum to the current row
            matrix[row].append(s)
        # add the final 1 to the row
        matrix[row].append(1)
        return matrix

numRows = 10
s = Solution()
a = s.generate(numRows)
print(a)