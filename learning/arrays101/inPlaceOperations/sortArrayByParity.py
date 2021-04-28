# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A. You may return any answer array that satisfies this condition.

# Example 1:
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Note:
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000

class Solution:
    def sortArrayByParity(self, A):
        front, back  = 0, len(A) - 1
        while front < back:
            while A[front] % 2 == 0 and front < len(A) - 1:
                front += 1
            while A[back] % 2 == 1 and back > -1:
                back -= 1
            if front < back:
                A[front], A[back] = A[back], A[front]
        return A

A = [1,2,1,2,1,2,1,2,1,2,1,2]
s = Solution()
a = s.sortArrayByParity(A)
print(a)