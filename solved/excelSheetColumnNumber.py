# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28

# Example 1:
# Input: "A"
# Output: 1

# Example 2:
# Input: "AB"
# Output: 28

# Example 3:
# Input: "ZY"
# Output: 701

# another way of writing the same thing as below
class Solution:
    def titleToNumber(self, s):
        num = 0
        for i in range(len(s)):
            num *= 26
            num += ord(s[i]) - ord("A") + 1
        return num

class mySolution:
    def titleToNumber(self, s):
        # create a dictionary using letters as key with numbers as corresponding values
        d = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
        # initiate a total value
        num = 0
        # iterate through the string
        for i in range(len(s)):
            # multiply the total value by 26
            num *= 26
            # add the value from the dictionary which corresponds with the key that matches the current iteration value in the string
            num += d[s[i]]
        # return the total value
        return num

s = "ZY"
sol = Solution()
a = sol.titleToNumber(s)
print(a)
