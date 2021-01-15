# Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

class Solution:
    def longestCommonPrefix(self, strs):
        # if there are no strings in the given array, return an empty string
        if len(strs) == 0:
            return ""
        # initialize a variable with an empty string to hold the answer
        prefix = ""
        # initialize a counter
        j = 0
        # loop the length of the first string in the array
        while j < len(strs[0]):
            # pick a letter for comparison, starting with the first and incrementing each loop
            letter = strs[0][j]
            # loop through the array
            for i in range(1, len(strs)):
                # check if the current string is long enough to have a letter for comparison
                if j < len(strs[i]):
                    # check if the current letter in the current string is equal to the comparison letter
                    # if it is not, then return the answer string
                    if strs[i][j] != letter:
                        return prefix
                # if the current string is out of letters, return the answer string
                else:
                    return prefix
            # after checking each string for the current letter, add that letter to the answer string
            prefix += letter
            # increment the comparison letter
            j += 1
        return prefix

strs = ["aspect", "respect", "pectoral"]
s = Solution()
a = s.longestCommonPrefix(strs)
print(a)