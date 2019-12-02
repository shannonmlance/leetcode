# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Note:
# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs):
        # if the array is empty, then return an empty string
        if len(strs) == 0:
            return ""
        # if the array contains only one string, then return that string
        if len(strs) == 1:
            return strs[0]
        # variable for holding the longest common prefix
        prefix = ""
        # find the shortest string and save it in a variable
        shortestWord = min(strs)
        # counter for iterating
        i = 0
        # repeat loop as long as the iterator is less than the length of the shortest string
        while i < len(shortestWord):
            # an array to store the letter from each string being compared
            letterArray = []
            # for each string in the given array
            for s in strs:
                # add the letter from the same position to the array storing those letters
                letterArray.append(s[i])
            # increment the counter
            i += 1
            # loop through the array storing the letters from the strings, exclude the last one
            for j in range(len(letterArray)-1):
                # compare the current letter with the next one, if they don't match, return the prefix variable
                if letterArray[j] != letterArray[j+1]:
                    return prefix
            # if all the letters in the array are the same, add that letter to the prefix variable
            prefix += letterArray[0]
        # if the shortest word matches the beginnings of all the other words, and the while loop has exited, then the prefix variable is complete and can be returned
        return prefix

strs = []
s = Solution()
a = s.longestCommonPrefix(strs)
print(a)

# looking at each string simultaneously, compare one letter at a time with the other strings
# stop when they are different
# be careful of strings that end before mismatch occurs