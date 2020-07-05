# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:
# Input: 16
# Output: true

# Example 2:
# Input: 5
# Output: false

# Follow up: Could you solve it without loops/recursion?

class Solution:
    def isPowerOfFour(self, num):
        # if the given number is greater than zero, then it could be a power of four
        # if the given number is divisible by four, then it could be a power of four. Convert the given number and the given number minus one to binary. Perform bitwise AND, which compares each bit in place. If corresponding bits, when multiplied, all equal zero, then the given number is divisible by four
        # if the length of the given number, in binary, is odd, then the given number could be a power of four. All powers of four, in binary, consist of a 1 followed by an even number of zeros
        # when all three conditions are true for the same given number, then the given number is a power of four
        return num > 0 and num & (num - 1) == 0 and len(bin(num)) % 2 == 1

class mySolution:
    def isPowerOfFour(self, num):
        if num < 1:
            return False
        while num > 1:
            if num % 1 != 0:
                return False
            num /= 4
        if num == 1:
            return True
        return False

num = 16
s = Solution()
a = s.isPowerOfFour(num)
print(a)

# bitwise powers of 4
# 4**0 =         1
# 4**1 =       100
# 4**2 =     10000
# 4**3 =   1000000
# 4**4 = 100000000
# must be a 1 with an even number of trailing zeros


# 4**0  =             1
# 4**1  =             4
# 4**2  =            16
# 4**3  =            64
# 4**4  =           256
# 4**5  =         1,024
# 4**6  =         4,096
# 4**7  =        16,384
# 4**8  =        65,536
# 4**9  =       262,144
# 4**10 =     1,048,576
# 4**11 =     4,194,304
# 4**12 =    16,777,216
# 4**13 =    67,108,864
# 4**14 =   268,435,456
# 4**15 = 1,073,741,824
