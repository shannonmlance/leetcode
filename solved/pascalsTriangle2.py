# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Note that the row index starts from 0.

# Example:
# Input: 3
# Output: [1,3,3,1]

class Solution:
    def getRow(self, rowIndex):
        # base case
        # if the requested row is 0, return that row, which is [1]
        if rowIndex == 0:
            return [1]
        # if the requested row is not 0
        else:
            # recursively find the previous row
            prev = self.getRow(rowIndex - 1)
            # initiate an array for the current row with the number 1
            cur = [1]
            # add each number in the previous row, except for the final number, to the next number and put the sum at the end of the current row's array
            for i in range(len(prev) - 1):
                cur.append(prev[i] + prev[i+1])
            # add a final 1 to the current row's array and return it
            cur.append(1)
            return cur

rowIndex = 5
s = Solution()
a = s.getRow(rowIndex)
print(a)