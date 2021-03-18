# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"

# Constraints:
# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.

class Solution:
    # helper method for reversing individual words
    def reverseWord(self, w):
        # initiate a variable for the reversed word
        wReversed = ""
        # loop backwards through the given word
        for i in range(len(w) - 1, -1, -1):
            # add the current value to the reversed word variable
            wReversed += w[i]
        return wReversed
    def reverseWords(self, s):
        # initiate a variable for the reversed word string
        sReversed = ""
        # initiate a variable for individual words
        word = ""
        # loop through the given string
        for i in range(len(s)):
            # if the current value is the last value in the string
            if i == len(s) - 1:
                # add the current value to the word variable
                word += s[i]
                # utilize helper method to reverse the current value in the word variable
                rw = self.reverseWord(word)
                # add the reversed word to the reversed word string
                sReversed += rw
            # if the current value is not the last value in the string, and if the current value is a space
            elif s[i] == " ":
                # utilize helper method to reverse the current value in the word variable
                rw = self.reverseWord(word)
                # add the reversed word to the reversed word string
                sReversed += rw
                # add a space to the reversed word string
                sReversed += " "
                # reset the word variable
                word = ""
            # if the current value is not the last value in the string, and if the current value is not a space
            else:
                # add the current value to the word variable
                word += s[i]
        return sReversed

s = "Let's take LeetCode contest"
sol = Solution()
a = sol.reverseWords(s)
print(a)