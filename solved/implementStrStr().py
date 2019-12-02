# Implement strStr(). Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview. For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack, needle):
        # set a loop for the length of the haystack, minus the length of the needle, plus one
        for i in range(len(haystack) - len(needle) + 1):
            # variable for comparing a substring of the haystack to the needle
            substr = ""
            # set a loop for the length of the needle
            for j in range(len(needle)):
                # add letters from the haystack to the substring for comparison
                substr += haystack[j+i]
            # if the substring from the haystack is the same as the needle
            if substr == needle:
                # return the index of the beginning of the substring of the haystack
                return i
        # if the whole haystack has been searched and the needle wasn't found, return -1
        return -1

class mySolution:
    def strStr(self, haystack, needle):
        # if the length of the needle is 0, or the needle matches the haystack exactly, return an index of 0
        if len(needle) == 0 or needle == haystack:
            return 0
        # if the length of the needle is more than the length of the haystack, then the needle cannot be in the haystack
        if len(needle) > len(haystack):
            return -1
        # set an iterator counter
        i = 0
        # as long as the iterator counter is less than the length of the haystack, keep searching for the needle
        while i < len(haystack):
            # if the current letter of the haystack is equal to the beginning of the needle
            if haystack[i] == needle[0]:
                # run a helper function to continue checking for match
                int = self.keepChecking(haystack, needle, i)
                # if the helper function returns a valid index number, then a match was found and the index number can be returned
                if int >= 0:
                    return int
            # increment the counter
            i += 1
        # if the whole haystack has been searched and the needle wasn't found, return -1
        return -1
    def keepChecking(self, haystack, needle, i):
        # set a loop for the length of the needle
        # no need to check the first letter as that has already been verified a match in the main function
        for j in range(1, len(needle)):
            # if the needle is still within the bounds of the haystack
            if i+j < len(haystack):
                # if the next haystack letter does not match the next needle letter, return -1
                if haystack[i+j] != needle[j]:
                    return -1
            # if the needle exceeds the length of the haystack, return -1
            else:
                return -1
        # if the entire needle is found in the haystack, return the index in the haystack of the first matching letter
        return i

haystack = "mississippi"
needle = "mississippies"
s = Solution()
a = s.strStr(haystack, needle)
print(a)

# loop through the haystack, looking for the first letter of the needle