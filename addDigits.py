# Given a non-negative integer num, repeatedly add all digits until the result has only one digit.

# Example:
# Input: 38
# Output: 2
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.

# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

class Solution:
    def addDigits(self, num):
        digit = num % 9
        if digit == 0:
            return 9
        return digit

# quick and easy solution
class easySolution:
    def addDigits(self, num):
        # base case
        # if the number already has only one digit, return that number
        if num < 10:
            return num
        # variable for holding the current sum of all digits
        sum = 0
        # as long as the number contains more than one digit
        while num > 9:
            # add the digit in the one's place to the sum variable
            sum += num % 10
            # divide the number by 10 to remove the current one's digit, and subsequently remove all digits after the decimal place
            num //= 10
        # recursively call the method, passing in the sum of all digits
        return self.addDigits(sum + num)

num = 50
s = Solution()
a = s.addDigits(num)
print(a)