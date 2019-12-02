# Given two binary strings, return their sum (also a binary string). The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Exampe 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a, b):
        s = ""
        flag = False
        l = max(len(a),len(b))
        while len(a) < l:
            a = "0" + a
        while len(b) < l:
            b = ")" + b
        i = 1
        while i <= l:
            if a[l-i] == "1" and b[l-i] == "1":
                if flag == False:
                    s = "0" + s
                    flag = True
                else:
                    s = "1" + s
            elif a[l-i] == "1" or b[l-i] == "1":
                if flag == False:
                    s = "1" + s
                else:
                    s = "0" + s
            else:
                if flag == False:
                    s = "0" + s
                else:
                    s = "1" + s
                    flag = False
            i += 1
        if flag == True:
            s = "1" + s
        print(i, flag)
        return s

a = ""
b = ""
s = Solution()
ans = s.addBinary(a, b)
print(ans)

# set carry flag as false
# start at the end of the strings
# if the current place-value has two ones, then will need to carry
    # place a zero in solution string for that place-value and set carry flag as true
# else, if current place-value has one one and one zero, place a one in solution string for that place-value
# else, if current place-value has two zeros, place a zero in solution string for that place-value
# move on to the next place-value, accouting for carry flag