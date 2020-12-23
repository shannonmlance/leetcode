# Implement strStr(). Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview. For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:
# Input: haystack = "", needle = ""
# Output: 0

# Constraints:
# 0 <= haystack.length, needle.length <= 5 * 104
# haystack and needle consist of only lower-case English characters.

class Solution:
    def strStr(self, haystack, needle):
        # if the needle is empty, there's nothing to compare
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            # if the needle is bigger than the haystack, the needle cannot be found in the haystack
            return -1
        # loop through the haystack, ending when the needle can no longer fit in the remaining haystack
        for i in range(len(haystack) - len(needle) + 1):
            # if the current letter in the haystack matches the first letter in the needle
            if haystack[i] == needle[0]:
                # initiate a pointer
                n = 1
                # loop through the haystack and the needle simultaneously
                # on each loop, check that the current letter in the haystack matches the current letter in the needle
                while n < len(needle) and i + n < len(haystack) and haystack[i + n] == needle[n]:
                    n += 1
                # when the loop ends, check if the loop completed or if it ended early due to mismatch
                if n == len(needle):
                    return i
        return -1

haystack = "mississippi"
needle = "issippi"
s = Solution()
a = s.strStr(haystack, needle)
print(a)