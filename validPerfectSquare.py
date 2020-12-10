# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

# Example 1:
# Input: num = 16
# Output: true

# Example 2:
# Input: num = 14
# Output: false

# Constraints:
# 1 <= num <= 2^31 - 1

class Solution:
    def isPerfectSquare(self, num):
        return bool
    # method for finding the square
    def sqrt(self, num):
        # break up the original number into two-digit chunks, starting at the ones place
        # initialize a counter for how many two-digit chunks the input number contains
        twoDigitChunks = 0
        # initialize a variable equal to the input number, so that the input number can be mutated without losing the original number
        chunkedNumber = num
        # loop to discover how many two-digit chunks are in the input number
        while chunkedNumber > 0:
            # remove the last two digits from the input number variable
            chunkedNumber = (chunkedNumber - (chunkedNumber % 100)) / 100
            # increment the two-digit chunk counter
            twoDigitChunks += 1
        # initialize variables
        workingNumber = 0
        squareRoot = 0
        remainder = 0
        # loop through the following process for each two-digit chunk
        for tdc in range(twoDigitChunks-1, -1, -1):
            # the current number to work with is equal to the remainder of the previous two-digit chunk (multiplied by 100) plus the current two-digit chunk of the original number, starting from the left
            workingNumber = (workingNumber * 100) + ((num - (num % (100 ** tdc))) // (100 ** tdc))
            # set the current remainder equal to the previous square root, times two
            
        return bool

num = 46295620184659
s = Solution()
a = s.isPerfectSquare(num)
print(a)