# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

# Example 1:
# Input: "III"
# Output: 3

# Example 2:
# Input: "IV"
# Output: 4

# Example 3:
# Input: "IX"
# Output: 9

# Example 4:
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 5:
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def romanToInt(self, s):
        # variable to store integer
        num = 0
        # dictionary for easy conversions from roman numerals into integers
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # iterator counter
        i = 0
        # loop through the roman numeral as long as the iterator counter is less than the length of the letters composing the roman numeral
        while i < len(s):
            # if the iterator counter is two less than the length of the letters composing the roman numeral, there is a possibility that a subtraction might be necessary
            if i < len(s)-1:
                # if the next letter is worth more than the current letter
                if d[s[i+1]] > d[s[i]]:
                    # subtract the next letter's worth from the current letter's worth, and add that to the integer variable
                    num += d[s[i+1]] - d[s[i]]
                    # move the iterator counter an additional step forward, to account for looking at both the current letter and the next letter, as they should be considered one number's worth
                    i += 1
                # otherwise
                else:
                    # add the current letter's worth to the integer variable
                    num += d[s[i]]
            # otherwise
            else:
                # add the current letter's worth to the integer variable
                num += d[s[i]]
            # move the iterator counter forward
            i += 1
        # return the integer that now equals the value of the roman numeral
        return num

# clunky solution
# same as above, only without the use of a dictionary, so each possibility was written out, causing a lot of repeated code
class mySolution:
    def romanToInt(self, s):
        num = 0
        i = 0
        while i < len(s):
            if s[i] == "M":
                num += 1000
            if s[i] == "D":
                num += 500
            if s[i] == "C":
                if i < len(s)-1:
                    if s[i+1] == "M":
                        num += 900
                        i += 1
                    elif s[i+1] == "D":
                        num += 400
                        i += 1
                    else:
                        num +=100
                else:
                    num += 100
            if s[i] == "L":
                num += 50
            if s[i] == "X":
                if i < len(s)-1:
                    if s[i+1] == "C":
                        num += 90
                        i += 1
                    elif s[i+1] == "L":
                        num += 40
                        i += 1
                    else:
                        num += 10
                else:
                    num += 10
            if s[i] == "V":
                num += 5
            if s[i] == "I":
                if i < len(s)-1:
                    if s[i+1] == "X":
                        num += 9
                        i += 1
                    elif s[i+1] == "V":
                        num += 4
                        i += 1
                    else:
                        num += 1
                else: num += 1
            i += 1
        return num

s = "IV"
solve = Solution()
a = solve.romanToInt(s)
print(a)

# create variables to store roman numeral equivalents
# iterate through the string, adding each numeral equivalent to the total
# account for if the next letter is more than the current letter, as that indicates the current number needs to be subtracted from the next, and then the difference is added to the total