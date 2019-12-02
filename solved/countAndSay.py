# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

# Example 1:
# Input: 1
# Output: "1"

# Example 2:
# Input: 4
# Output: "1211"

class Solution:
    def countAndSay(self, n):
        # base case is reached when input is equal to 1
        if n == 1:
            # when input is equal to 1, the return is always "1"
            bc = "1"
            return bc
        # anything other than input equals 1 is not a base case and will need to be answered recursively
        else:
            # as each solution is based on the one directly prior, recursively call the method, passing in the input's previous number
            prev = self.countAndSay(n-1)
            # initialize a variable to track how many numbers in a row are the same. As there will always be at least one of each number in the answer, set variable to one
            count = 1
            # generate an empty string to build the answer
            say = ""
            # initialize an iterator counter, starting at the second index
            i = 1
            # as long as the iterator is less than the length of the string returned from the recursive call
            while i < len(prev):
                # if the current index's value and the previous index's value in the string returned from the recursive call are the same, increment the variable storing how many numbers in a row are the same
                if prev[i] == prev[i-1]:
                    count += 1
                # if the current index's value and the previous index's value in the string returned from the recursive call are not the same
                else:
                    # add the current count of how many numbers in a row were the same and that number to the answer
                    say += str(count) + prev[i-1]
                    # reset the variable counting how many numbers in a row are the same back to one, as now there is a different number
                    count = 1
                # increment the iterator counter
                i += 1
            # once all numbers in the string returned from the recursive call have been compared to their neighbors and counted, add the last count of duplicates along with the number that was duplicated to the answer
            say += str(count) + prev[i-1]
            return say

n = 11
s = Solution()
a = s.countAndSay(n)
print(a)
