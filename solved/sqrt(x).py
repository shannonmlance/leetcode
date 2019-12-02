# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer. Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Example 1:
# Input: 4
# Output: 2

# Example 2:
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

import math

class Solution:
    def mySqrt(self, x):
        # quick exit, if the input number is zero, then the square root will be zero
        if x == 0:
            return 0
        # quick exit, if the input number is one, then the square root will be one
        if x == 1:
            return 1

        # break up the original number into chunks of two numbers, starting at the ones place
        # initialize a counter for how many two-number chunks the input number contains
        chunks = 0
        # set a variable equal to the input number, so that the input number can be mutated without losing the original number
        cx = x
        # loop for mutating the input number
        while cx > 0:
            # remove the lsat two digits from the input number
            cx = (cx - (cx % 100)) / 100
            # increment the two-number chunks counter
            chunks += 1
        # initialize variables
        num = 0
        sqr = 0
        rem = 0
        # loop through this process for each two-number chunk
        for c in range(chunks-1, -1, -1):
            # current number to work with is equal to the remainder of the previous two-number chunk (slid so that it ends in two zeros) plus the current two-number chunk of the original number, starting from the left
            num = (num * 100) + math.floor((x - (x % (100 ** c))) / (100 ** c))
            # set the current remainder equal to the previous square root, times two
            rem = sqr * 2
            # iterator for locating the next square root
            i = 0
            # loop to find the next square root
            while i <= num:
                # if the remainder (slid so that it ends in one zero) plus the next square root, multiplied by the next square root, is equal to the current number, then the iterator's value is the next square root
                if ((rem * 10) + i) * i == num:
                    break
                # if the remainder (slid so that it ends in one zero) plus the next square root, multiplied by the next square root, is more than the current number, then the iterator's previous value is the next square root
                if ((rem * 10) + i) * i > num:
                    i -= 1
                    break
                # increment the iterator until a square root is located
                i += 1
            # the square root is equal to the previous square root (slid so that it ends in one zero) plus the new square
            sqr = (sqr * 10) + i
            # subtract the remainder (slid so that it ends in one zero) plus the new square root, multiplied by the new square root, from the current number
            num -= ((rem * 10) + i) * i
            # remove a chunk from the input number, starting from the left
            x = math.floor(x % (100 ** c))
        # return the final square root value
        return sqr

# brute force solution
class mySolution:
    def mySqrt(self, x):
        # initialize the square root
        i = 0
        # loop to find square root
        while i <= x:
            # if the square root, squared, is equal to the input number, then the square root has been found
            if i * i == x:
                return i
            # if the square root, squared, is more than the input number, then the previous number was the square root
            if i * i > x:
                return i - 1
            # increment the square root
            i += 1

x = 0
s = mySolution()
a = s.mySqrt(x)
print(a)