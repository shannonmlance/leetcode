# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
 
# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution:
    def addBinary(self, a, b):
        # initialize an empty string for the answer, which will initially be reversed
        rs = ""
        # initialize variables equal to the lengths of both given strings
        i = len(a) - 1
        j = len(b) - 1
        # initialize a flag to indicate if the previous iteration had a leftover
        carry = False
        # loop until the shortest string is complete
        while i >= 0 and j >= 0:
            # lots of checks for which number to append to the string variable
            # 0 + 0 = 0
            # 1 + 0 = 1
            # 0 + 1 = 1
            # 1 + 1 = 10 (add a 0 to the string and set the carry flag to true)
            # 1 + 1 + 1 = 11 (if the flag is true and a and b are both 1, add a 1 to the string and leave the carry flas as true)
            if a[i] == "0":
                if b[j] == "0":
                    if carry:
                        rs += "1"
                        carry = False
                    else:
                        rs += "0"
                else:
                    if carry:
                        rs += "0"
                    else:
                        rs += "1"
            else:
                if b[j] == "0":
                    if carry:
                        rs += "0"
                    else:
                        rs += "1"
                else:
                    if carry:
                        rs += "1"
                    else:
                        rs += "0"
                        carry = True
            i -= 1
            j -= 1
        # while there are still numbers to evaluate in string a
        # same checks as above, but only between a and carry flag
        while i >= 0:
            if a[i] == "0":
                if carry:
                    rs += "1"
                    carry = False
                else:
                    rs += "0"
            else:
                if carry:
                    rs += "0"
                else:
                    rs += "1"
            i -= 1
        # while there are still numbers to evaluate in string b
        # same checks as above, but only between b and carry flag
        while j >= 0:
            if b[j] == "0":
                if carry:
                    rs += "1"
                    carry = False
                else:
                    rs += "0"
            else:
                if carry:
                    rs += "0"
                else:
                    rs += "1"
            j -= 1
        # if there is a carry after both strings are complete, add a final 1 to the string
        if carry:
            rs += "1"
        # initiate an empty string for the final answer
        s = ""
        # reverse the string
        for r in range(len(rs)-1, -1, -1):
            s += rs[r]
        return s

a = "1010"
b = "1011"
s = Solution()
a = s.addBinary(a, b)
print(a)