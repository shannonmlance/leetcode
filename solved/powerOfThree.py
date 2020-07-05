# Given an integer, write a function to determine if it is a power of three.

# Example 1:
# Input: 27
# Output: true

# Example 2:
# Input: 0
# Output: false

# Example 3:
# Input: 9
# Output: true

# Example 4:
# Input: 45
# Output: false

# Follow up:
# Could you do it without using any loop / recursion?

class Solution:
    def isPowerOfThree(self, n):
        # if the given number is negative or equal to zero, it cannot be a power of three
        # the largest power of three integer is 3**19
        # if 3**19, when divided by the given number has a remainder of zero, then it is a power of three
        return n > 0 and (3**19 % n == 0)

n = 0.128
s = Solution()
a = s.isPowerOfThree(n)
print(a)