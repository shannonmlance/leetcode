# Given an integer n, return the number of trailing zeros in n!.

# Example 1:
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zeros.

# Example 2:
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.

# Note:
# Your solution should be in logarithmic time complexity.

import math

class Solution:
    def trailingZeroes(self, n):
        # initiate a variable to count how many zeros
        x = 0
        # loop until the given number becomes zero
        while n != 0:
            # increment the count-zeros variable proportionally to the result of the given number divided by five, exclusive of remainders
            x += n // 5
            # divide the given number by five, discarding any remainder
            n //= 5
        # return the count-zeros variable
        return x

# should work, but the factorial get too big and the process breaks
class mySolution:
    def trailingZeroes(self, n):
        print("running trailing")
        f = self.factorial(n)
        print("F:", f)
        print("*"*10)
        count = 0
        trail = 0
        while trail == 0:
            print("trail still is 0")
            trail = f % 10
            f = math.floor(f/10)
            print("new f:", f)
            print("incremented count")
            count += 1
        return count - 1
    def factorial(self, n):
        print("running factorial")
        f = 1
        while n > 0:
            f *= n
            n -= 1
        return f

n = 482916559203
s = Solution()
a = s.trailingZeroes(n)
print("~"*10)
print(a)