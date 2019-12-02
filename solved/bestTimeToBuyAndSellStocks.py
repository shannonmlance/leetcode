# Say you have an array for which the ith element is the price of a given stock on day i. If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.

# Example 2:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

class Solution:
    def maxProfit(self, prices):
        # if less than two numbers are submitted, there can be no profit
        if len(prices) < 2:
            return 0
        # initialize variables for maximum profit and highest selling point
        mp = 0
        high = 0
        # loop backwards through the array
        # looping backwards allows for finding the highest selling point first, and then comparing profits with each iteration
        for p in range(len(prices) - 1, -1, -1):
            # if the current value is greater than the highest selling point variable, set the value of the highest selling point variable as the current value
            if prices[p] > high:
                high = prices[p]
            # if the difference between the highest selling point variable and the current value is greater than the maximum profit variable, set the value of the maximum profit variable as the difference between the highest selling point variable and the current value
            # this can be an else-if instead of just an if, because if the prior if is true, then the difference between the highest selling point variable and the current value will always equal zero, which is the initial value of the maximum profit
            elif high - prices[p] > mp:
                mp = high - prices[p]
        return mp

# times out
class mySolution:
    def maxProfit(self, prices):
        print("running main method")
        if len(prices) < 2:
            print("less than 2 values")
            return 0
        mp = 0
        for i in range(len(prices) - 1):
            print("buying at", prices[i])
            for j in range(i+1, len(prices)):
                print("selling at", prices[j])
                if prices[j] - prices[i] > mp:
                    mp = prices[j] - prices[i]
                    print("found a new max price:", mp)
        return mp

prices = [1,2]
s = Solution()
a = s.maxProfit(prices)
print(a)