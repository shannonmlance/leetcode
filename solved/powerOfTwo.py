# Given an integer, write a function to determine if it is a power of two.

# Example 1:
# Input: 1
# Output: true 
# Explanation: 2**0 = 1

# Example 2:
# Input: 16
# Output: true
# Explanation: 2**4 = 16

# Example 3:
# Input: 218
# Output: false

class Solution:
    def isPowerOfTwo(self, n):
        # as long as the given number is more than 1
        while n > 1:
            # if the given number is not an integer, then it cannot be the result of a power of two
            if n % 1 != 0:
                return False
            # divide the given number in half
            n = n / 2
        # once the given number is equal to, or less than, one, then the original given number is a result of a power of two
        if n ==  1:
            return True
        # if it's not exactly one, then it can't be a power of two
        return False

# 2**0 = 1
# 2**1 = 2
# 2**2 = 4
# 2**3 = 8
# 2**4 = 16
# 2**5 = 32
# 2**6 = 64
# 2**7 = 128
# 2**8 = 256
# 2**9 = 512
# 2**10 = 1024
# 2**11 = 2048

n = 3
s = Solution()
a = s.isPowerOfTwo(n)
print(a)