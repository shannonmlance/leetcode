# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [-2^31, (2^31)-1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# needed for running on leetcode, not needed locally
import math

class Solution:
    def reverse(self, x):
        # if the input number only contains one digit, there is no need to reverse the number
        if -10 < x < 10:
            # return the original number
            return x
        # set 32-bit signed integer limit (using only the positive number since we remove the negative sign later)
        limit = 2147483647
        # flag for remembering if the number was negative prior to reversing it
        neg = False
        # check if number is negative
        if x < 0:
            # set flag accordingly
            neg = True
            # make number positive
            x *= -1
        # initialize reverse variable
        rev = 0
        # repeat the reversing process until all numbers have been used
        while x > 0:
            # variable for holding the number that is currently occupying the ones place
            digit = x % 10
            # check if adding the removed number to the current reversal will cause overflow
            if ((limit - (rev * 10) < digit) and neg == False) or ((limit - (rev * 10) < digit - 1) and neg == True):
                # return nothing due to overflow
                return 0
            # add the removed number to the current reversal
            rev = (rev * 10) + digit
            # remove the removed number from the original number
            x = (x - digit) / 10
        # check if the original number was negative
        if neg:
            # make the number negative
            rev *= -1
        # return the reversed number, math.floor() was necessary for leetcode, not needed locally
        return math.floor(rev)

s = Solution()
x = 5
a = s.reverse(x)
print(a)

# set flag for negative number, and remove negative
# remove number from the ones column using %, subtraction, and division by 10.
# place removed number into variable number, multiplying by 10 and adding in new number
    # set up safeguards to exit out if overflow will occur upon additon
# continue this process until the original number is 0
# if flagged as negative, add back in the negative
# return newly reversed number