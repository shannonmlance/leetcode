# Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space. Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

# Example 4:
# Input: s = "  Bob    Loves  Alice   "
# Output: "Alice Loves Bob"

# Example 5:
# Input: s = "Alice does not even like bob"
# Output: "bob like even not does Alice"

# Constraints:
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.

class Solution:
    def reverseWords(self, s):
        # initiate variables, one for storing individual words, and one for storing all words in the string
        word = ""
        sArr = []
        # loop through given string
        for i in range(len(s)):
            # if the current value is the last value in the string
            if i == len(s) - 1:
                # if the value not a space
                if s[i] != " ":
                    # add the value to the word variable
                    word += s[i]
                # if the word variable is not empty
                if len(word) > 0:
                    # add the word to the word array
                    sArr.append(word)
            # if the current value is not the last value in the string, and if the current value is a space
            elif s[i] == " ":
                # if the word variable is not empty
                if len(word) > 0:
                    # add the word to the word array
                    sArr.append(word)
                # reset the word variable
                word = ""
            # if the current value is not the last value in the string, and if the current value is not a space
            else:
                # add the value to the word variable
                word += s[i]
        # initiate a variable to build the reversed string
        sReverse = ""
        # loop backwards through the word array, except for the final value
        for i in range(len(sArr) - 1, 0, -1):
            # add the value to the reversed string variable
            sReverse += sArr[i]
            # add a space to the reversed string variable
            sReverse += " "
        # add the final value from the word array to the reversed string variable
        sReverse += sArr[0]
        return sReverse

s = "  Bob     Loves  /alice   "
sol = Solution()
a = sol.reverseWords(s)
print(a)