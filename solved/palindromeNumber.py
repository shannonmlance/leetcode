# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:
# Input: 121
# Output: True

# Example 2:
# Input: -121
# Output: False
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: 10
# Output: False
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Follow up:
# Could you solve it without converting the integer to a string?

import math

# my optimized solution
class Solution:
    def isPalindrome(self, x):
        # if the original number is negative, it cannot be a palindrome
        if x < 0:
            return False
        # if the original number contains only one digit, it will always be a palindrome
        if 0 <= x < 10:
            return True
        # if the original number has a zero in the ones place, it cannot be a palindrome
        if x % 10 == 0:
            return False
        # set a variable for tracking the reversal of the original number
        rev = 0
        # loop through the reversal until the reversed number is bigger than the modified original number
        while rev < x:
            # variable for retaining the digit occupying the ones place
            digit = x % 10
            # put the store digit into the ones place of the reversed number, moving all other digits up one place
            rev = (rev * 10) + digit
            # remove the digit from the ones place in the original number, and move all other digits down one place
            x = math.floor((x - digit) / 10)
        # once the loop is finished, if the reversed number matches the modified original number, or if the reversed number without its digit in the ones place matches the modified original number, than the original number was a palindrome
        if x == rev or x == math.floor((rev - (rev % 10)) / 10):
            return True
        # if there isn't a match, then it wasn't a palindrome
        return False

# my original solution
class mySolution:
    def isPalindrome(self, x):
        # if original number is negative, it cannot be a palindrome
        if x < 0:
            return False
        # if the original number only contains one digit, it will always be a palindrome
        if 0 <= x < 10:
            return True
        # if the original number has a zero in the ones place, it cannot be a palindrome
        if x % 10 == 0:
            return False
        # set counter variable for counting how many digits are in the number
        count = 0
        # set variable for mutating the original number, while still being able to reference the original number later
        cx = x
        # loop until the mutating number is zero
        while cx > 0:
            # remove the last digit from the mutating number
            cx = (cx - (cx % 10)) / 10
            # increment the digit counter
            count += 1
        # loop for removing external numbers from the original number
        for c in range(count, 1, -2):
            # remove the first digit from the original number and store the modified original number in a variable
            fx = x % (10 ** (c - 1))
            # use the modified original number to isolate the first digit of the original number
            f = math.floor((x - fx) / (10 ** (c - 1)))
            # set the modified original number as the new number to work with
            x = fx
            # isolate the last digit
            l = x % 10
            # remove the last digit
            x = math.floor((x - l) / 10)
            # if the first and last digit from the original number are the not the same, it cannot be a palindrome
            if f != l:
                return False
        # if the number makes it this far, then all the digits, starting from both ends, have a match and the number is a palindrome
        return True

x = 12321
s = Solution()
a = s.isPalindrome(x)
print(a)

# if the number is negative, it is not a palindrome
# if the number has a 0 in the ones place, it is not a palindrome
# if the number has only one digit, it is a palindrome

# count how many digits there are in the number
# starting at both ends, see if the numbers are the same