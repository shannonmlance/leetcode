# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.

# changes full array into just two variables
class goodSolution:
    def rob(self, nums):
        # if the given array is empty, return zero
        if len(nums) == 0:
            return 0
        # set two variables to store the two highest options
        prev1 = 0
        prev2 = 0
        # iterate through the given array
        for n in nums:
            # store one option in a variable
            temp = prev1
            # update that option by comparing it to the other option plus the current value
            prev1 = max(prev2 + n, temp)
            # update the other option
            prev2 = temp
        # return the highest option
        return prev1

# sill requires an entire array
# aka dynamic programming
class iterativeMemoizationSolution:
    def rob(self, nums):
        # if the given array is empty, there is no total
        if len(nums) == 0:
            return 0
        # utilize an array to track the maximum
        memo = []
        # set the first value as zero, to prevent out-of-range errors
        memo.append(0)
        # set the second value as the first value of the given array, since currently it is the maximum value
        memo.append(nums[0])
        # iterate through the given array
        for i in range(1,len(nums)):
            # compare the current value plus skip two with the skip one value and add the maximum to the maximum array
            memo.append(max(memo[i], memo[i-1] + nums[i]))
        # the final value in the maximum array will be the largest possible amount
        r = memo[len(nums)]
        return r

# has a recursive stack
class recursiveMemoizationSolution:
    def rob(self, nums):
        # utilize an array to remember previous recursive calls
        memo = []
        # fill array with negative numbers
        for i in range(len(nums)+1):
            memo.append(-1)
        # call  recursive function which calculates the maximum between skip one and skip two
        r = self.robr(memo, nums, len(nums)-1)
        return r
    def robr(self, memo, nums, i):
        # base case
        # if i (length of nums array) is less than zero, return zero
        if i < 0:
            return 0
        # base case
        # if the value in the array for i has a zero or positive value, return that amount
        # this is where we prevent calculating the same value multiple times
        if memo[i] >= 0:
            return memo[i]
        # recursively find the maximum between teh current value plus skip two and skip one
        r = max(self.robr(memo, nums, i-2) + nums[i], self.robr(memo, nums, i-1))
        memo[i] = r
        return r

# calculates the same number multiple times
class recursiveSolution:
    def rob(self, nums):
        # call recursive function which calculates the maximum between skip one and skip two
        r = self.robr(nums, len(nums)-1)
        return r
    def robr(self, nums, i):
        # base case
        # if i (length of nums array) is less than zero, return zero
        if i < 0:
            return 0
        # recursively find the maximum between the current value plus skip two and skip one
        r = max(self.robr(nums, i-2) + nums[i], self.robr(nums, i-1))
        return r

nums = [99,98,3,5,6]
s = Solution()
a = s.rob(nums)
print(a)