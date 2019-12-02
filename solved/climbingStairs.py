# You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
    # 1. 1 step + 1 step
    # 2. 2 steps

# Example 2:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
    # 1. 1 step + 1 step + 1 step
    # 2. 1 step + 2 steps
    # 3. 2 steps + 1 step

import math

# uses fibonacci formula to solve the problem
# as this is direct mathematical formula, no recursion or binary search is necessary
# time: O(1) - can be argued that pow function takes O(log n)
# space:O(1)
class Solution:
    def climbStairs(self, n):
        if n == 0:
            return 0
        sqrt5 = math.sqrt(5)
        fibn = (((1 + sqrt5) / 2) ** (n + 1)) - (((1 - sqrt5) / 2) ** (n + 1))
        a = math.floor(fibn / sqrt5)
        return a

# uses Binet's method to solve the problem
# this is a binary search method using a matrix, which allows a much faster run time
# time: O(log n)
# space: O(1)
class binSolution:
    def climbStairs(self, n):
        q = [[1,1],[1,0]]
        res = self.pow(q, n)
        return res[0][0]
    def pow(self, a, n):
        ret = [[1,0],[0,1]]
        while n > 0:
            if n % 2 == 1:
                ret = self.multiply(ret, a)
            n = math.floor(n/2)
            a = self.multiply(a, a)
        return ret
    def multiply(self, a, b):
        c = [[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c

# uses the traditional fibonacci solution to solve the problem
# uses less memory because everything is done in place with limited variables, no array needed for retrieval
# time: O(n)
# space: O(1)
class fibSolution:
    def climbStairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        first = 1
        second = 2
        i = 3
        while i <= n:
            third = first + second
            first = second
            second = third
            i += 1
        return third

# uses dynamic programming to solve the problem
# not any better than the memoization way, but does not require recursion
# time: O(n)
# space: O(n)
class dpSolution:
    def climbStairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = []
        for i in range(n+1):
            dp.append(0)
        dp[1] = 1
        dp[2] = 2
        i = 3
        while i <= n:
            dp[i] = dp[i-1] + dp[i-2]
            i += 1
        return dp[n]

# uses memoization to solve the problem
# takes less time because the recursive answers are stored in an array, avoids repeating the same recursive call
# time: O(n)
# space: O(n)
class memoSolution:
    def climbStairs(self, n):
        if n == 0:
            return 0
        memo = []
        for i in range(n):
            memo.append(0)
        climbed = self.climbing(0, n, memo)
        return climbed
    def climbing(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climbing(i+1, n, memo) + self.climbing(i+2, n, memo)
        return memo[i]

# uses recursion to solve the problem
# time: O(2^n)
# space: O(n)
class longSolution:
    def climbStairs(self, n):
        if n == 0:
            return 0
        climbed = self.climbing(0, n)
        return climbed
    def climbing(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        climbed = self.climbing(i + 1, n) + self.climbing(i + 2, n)
        return climbed

n = 8
s = Solution()
a = s.climbStairs(n)
print(a)
