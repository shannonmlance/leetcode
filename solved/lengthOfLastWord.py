# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:
# Input: "Hello World"
# Output: 5

class Solution:
    def lengthOfLastWord(self, s):
        # initiate variable for counting how many letters in last word
        int = 0
        # loop backwards through the string
        for i in range(len(s)-1, -1, -1):
            # if the current value is a space and at least one letter has been found, then the last word has been completely accounted for, so return the number of letters in that last word
            if s[i] == " " and int > 0:
                return int
            # if the current value is not a space, then it must be part of the last word, so increment the letter counter
            if s[i] != " ":
                int += 1
            # the only other option is that the current value is a space and no letters have yet been found << if s[i] == " ": >> However, there is no need to account for this option, as if this condition is met, there would be no action taken, aside from continuing to iterate through the string, continuing to look for a letter
        return int

s = "a "
sol = Solution()
a = sol.lengthOfLastWord(s)
print(a)