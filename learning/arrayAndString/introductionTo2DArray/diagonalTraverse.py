# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
# Explanation:
# - start at the first index of the first array  [1]
# - move right (to the second index of the first array) and move diagonally down and left (first index of the second array) [2,4]
# - move down (to the first index of the third array) and move diagonally up and right (second index of the second array, third index of the first array) [7,5,3]
# - move right (out of index) and move diagonally down and left (third index of the second array, second index of the third array) [6,8]
# - move down (out of index) and move diagonally up and right (third index of the third array) [9]

class Solution:
    def findDiagonalOrder(self, matrix):
        # initiate an empty dictionary
        d = {}
        # loop through the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # if the index value is already in the dictionary as a key
                if i+j in d:
                    # each key in the dictionary has an array as its value
                    # add the current matrix value to the dictionary, using the index value as the key
                    d[i+j].append(matrix[i][j])
                # if the index value is not already in the dictionary as a key
                else:
                    # add the current matrix value to an array in the dictionary, using the index value as the key
                    d[i+j] = [matrix[i][j]]
        # initiate an empty array
        arr = []
        # loop through the dictionary, pulling the keys in order
        for x in range(len(d)):
            # if the key is an odd number
            if x % 2 == 1:
                # loop through the array associated with the key
                for i in d[x]:
                    # add each value from the key's array to the new array
                    arr.append(i)
            # if the key is an even number
            else:
                # reverse the array associated with the key
                d[x].reverse()
                # loop through the array associated with the key
                for i in d[x]:
                    # add each value from the key's array to the new array
                    arr.append(i)
        return arr

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
s = Solution()
a = s.findDiagonalOrder(matrix)
print(a)

class mySolution:
    def findDiagonalOrder(self, matrix):
        # if the matrix is empty, return an empty array
        if len(matrix) == 0:
            return []
        # initiate an empty array
        arr = []
        # initiate two markers for traversing the given array, one for height and one for width, with a value of zero
        # also initiate a variable for counting diagonal passes made through the given array, with a value of zero
        i = j = turn = 0
        # while the diagonal passes variable has a value less than the sum of the height and width of the matrix minus one
        while turn < (len(matrix) + len(matrix[0]) - 1):
            # if this is the first diagonal pass through the matrix
            if turn == 0:
                # add the first value of the first array in the matrix to the empty array
                arr.append(matrix[i][j])
            # if this is not the first diagonal pass through the matrix and the diagonal passes variable has an odd value
            elif turn % 2 == 1:
                # if the diagonal passes variable has a value less than the width of the matrix (length of the arrays within the matrix)
                if turn < len(matrix[0]):
                    # increment the width marker
                    j+= 1
                    # add the current value of the matrix markers to the array variable
                    arr.append(matrix[i][j])
                # if the diagonal passes variable has a value that is not less than the width of the matrix (length of the arrays within the matrix)
                if turn >= len(matrix[0]):
                    # increment the heighth marker
                    i += 1
                    # add the current value of the matrix markers to the array variable
                    arr.append(matrix[i][j])
                # while the width marker is greater than zero, and the heighth marker is less than the length of the matrix minus one
                while j > 0 and i < len(matrix) - 1:
                    # increment the heighth marker and decrement the width marker
                    i += 1
                    j -= 1
                    # add the current value of the matrix markers to the array variable
                    arr.append(matrix[i][j])
            # if this is not the first diagonal pass through the matrix and the diagonal passes variable has an even value
            elif turn % 2 == 0:
                # if the diagonal passes variable has a value less than the heighth of the matrix (length of the matrix)
                if turn < len(matrix):
                    # increment the heighth marker
                    i += 1
                    # add the current value of the matrix markers to the array variable
                    arr.append(matrix[i][j])
                # if the diagonal passes variable has a value that is not less than the heighth of the matrix (length of the matrix)
                if turn >= len(matrix):
                    # increment the width marker
                    j += 1
                    # add the current value of the matrix markers to the array variable
                    arr.append(matrix[i][j])
                # while the heighth marker is greater than zero, and the width marker is less than the length of the arrays within the matrix minus one
                while i > 0 and j < len(matrix[0]) -  1:
                    # decrement the heighth marker and increment the width marker
                    i -= 1
                    j += 1
                    # add the current value of the matrix markers to the array variable
                    arr.append(matrix[i][j])
            # increment the diagonal passes variable
            turn += 1
        return arr

