# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

import math

class Solution:
    def spiralOrder(self, matrix):
        # if the matrix is empty, or if the interior arrays are empty, return an empty array
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        # initiate an empty array to return
        arr = []
        # initiate variables for the size of the matrix
        height = len(matrix)
        width = len(matrix[0])
        # determine how many circles will need to be completed
        circles = math.ceil(min(height, width)/2)
        # determine if one of the circles will only be a half circle
        half = math.floor(min(height, width)/2)
        # loop through each circle
        for c in range(circles):
            # set beginning circle coordinates to the size of the circle, out to in
            i = j = c
            # add the first value of the circle to the return array
            arr.append(matrix[i][j])
            # loop until reaching the rightmost edge of the square, adjusted depending on which circle is being completed
            while j < width - 1 - c:
                # move right and add each value of the circle to the return array
                j += 1
                arr.append(matrix[i][j])
            # loop until reaching the bottommost edge of the square, adjusted depending on which circle is being completed
            while i < height - 1 - c:
                # move down and add each value of the circle to the return array
                i += 1
                arr.append(matrix[i][j])
            # if the the final circle is only a half circle, and this is the final loop, break here and return the array
            if half != circles and c == circles - 1:
                return arr
            # loop until reaching the leftmost edge of the square, adjusted depending on which circle is being completed
            while j > 0 + c:
                # move left and add each value of the circle to the return array
                j -= 1
                arr.append(matrix[i][j])
            # loop until reaching the uppermost edge of the square, minus one since that was the beginning value, adjusted depending on which circle is being completed
            while i > 0 + c + 1:
                # move up and add each value of the circle to the return array
                i -= 1
                arr.append(matrix[i][j])
        return arr
    # method for quickly building a matrix of any size
    def buildMatrix(self, height, width):
        matrix = []
        num = 1
        for i in range(height):
            matrix.append([])
            for j in range(width):
                matrix[i].append(num)
                num += 1
        return matrix

s = Solution()
matrix = s.buildMatrix(5,5)
a = s.spiralOrder(matrix)
print(a)