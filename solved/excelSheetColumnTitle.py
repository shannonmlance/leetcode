# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# For example:
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB

# Example 1:
# Input: 1
# Output: "A"

# Example 2:
# Input: 28
# Output: "AB"

# Example 3:
# Input: 701
# Output: "ZY"

import math

class Solution:
    def convertToTitle(self, n):
        # initiate a variable containing alphabet for reference
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # initiate an empty string for answer
        a = ""
        # continue to loop until the given number is zero
        while n > 0:
            # start by subtracting one from the given number, as there is no letter that corresponds with zero
            # this must be done for each loop, because of the absence of "zero letter" each time a letter is added to the answer
            n -= 1
            # determine the value that will correspond with the current letter
            i = n % 26
            # add that letter from the alphabet variable to the beginning of the answer
            a = alpha[i] + a
            # modify the given number by removing the value that corresponded to the current letter, and divide the answer by twenty-six, since we have found a letter for that loop
            n = math.floor((n - i)/26)
        return a

n = 704
s = Solution()
a = s.convertToTitle(n)
print(a)