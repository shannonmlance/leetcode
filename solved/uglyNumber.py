# Write a program to check whether a given number is an ugly number. Ugly numbers are positive numbers whose prime factors only include 2, 3, and 5.

# Example 1:
# Input: 6
# Output: true
# Explanation: 6 = 2 x 3

# Example 2:
# Input: 8
# Output: true
# Explanation: 8 = 2 x 2 x 2

# Example 3:
# Input: 14
# Output: false
# Explanation: 14 is not ugly since it includes another prime factor, 7.

# Notes:
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range [-2^31, 2^31 - 1].

class Solution:
    def isUgly(self, num):
        # if the given number is negative or zero, then it is not an ugly number
        if num < 1: return False
        # if the given number is between zero and seven, then it is an ugly number as it only has prime factors of 1, 2, 3, and 5
        if num < 7: return True
        # factor out all 2s
        while num % 2 == 0:
            num //= 2
        # factor out all 3s
        while num % 3 == 0:
            num //= 3
        # factor out all 5s
        while num % 5 == 0:
            num //= 5
        # if the number is now 1, then it is an ugly number
        if num == 1:
            return True
        # if the number is something other than 1, then it is not an ugly number
        else:
            return False

num = 210
s = Solution()
a = s.isUgly(num)
print(a)