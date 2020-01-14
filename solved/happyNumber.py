# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example 1: 

# Input: 19
# Output: true
# Explanation: 
# 1**2 + 9**2 = 1 + 81 = 82
# 8**2 + 2**2 = 64 + 4 = 68
# 6**2 + 8**2 = 36 + 64 = 100
# 1**2 + 0**2 + 0**2 = 1 + 0 + 0 = 1

# Example 2:
# Input: 20
# Output:
# Explanation:
# 2**2 + 0**2 = 4 + 0 = 4
# 4**2 = 16
# 1**2 + 6**2 = 1 + 36 = 37
# 3**2 + 7**2 = 9 + 49 = 58
# 5**2 + 8**2 = 25 + 64 = 89
# 8**2 + 9**2 = 64 + 81 = 145
# 1**2 + 4**2 + 5**2 = 1 + 16 + 25 = 42
# 4**2 + 2**2 = 16 + 4 = 20

class Solution:
    def isHappy(self, n):
        # initiate a slow runner with a value equal to the given number
        slow = n
        # initiate a fast runner with a value equal to the summation of the squares of the digits of the given number
        fast = self.sumsUp(n)
        # loop until either the fast runner equals one or the two runners are equal
        while fast != 1 and slow != fast:
            # adjust the slow runner to equal the summation of the squares of the digits of itself
            slow = self.sumsUp(slow)
            # adjust the fast runner to equal the summation of the squares of the digits of the summation of the squares of the digits of itself
            fast = self.sumsUp(self.sumsUp(fast))
        # if fast equals one, return true
        # if fast does not equal one, return false
        return fast == 1
    # helper function to find the summation of the squares of the digits of a given number
    def sumsUp(self, n):
        # initiate a variable to store the summation of the squares of the digits of the given number
        s = 0
        # loop until the given number is zero
        while n != 0:
            # initiate a variable equal to the one's place digit of the given number
            d = n % 10
            # remove the one's place digit from the given number, thereby sliding all numbers down one place value
            n = n//10
            # add the square of the one's place digit to the sum
            s += d**2
        # return the sum
        return s

class mySolution:
    def isHappy(self, n):
        # initiate variable for storing the original input value
        num = n
        # initiate variable for storing the summation of the squares of the digits of a number
        s = 0
        # initiate empty dictionary to store previously seen summations
        kv = {}
        # loop through until summation equals one
        while s != 1:
            # reset summation to zero each loop
            s = 0
            # loop through until given number equals zero
            while n != 0:
                # initiate variable for retrieving one's place digit from given number
                d = n % 10
                # remove one's place digit from given number, thereby sliding all numbers down one place value
                n = (n - d)/10
                # add the square of the one's place digit to the sum
                s += d**2
            # reset the given number to equal the sum
            n = s
            # check if the sum has already been seen, thereby indicating a loop
            if n in kv:
                return False
            # store the sum in the dictionary
            kv[n] = n
        # if the loop exited, then the summation was able to reach a value of one
        return True
    
n = 213
s = Solution()
a = s.isHappy(n)
print(a)