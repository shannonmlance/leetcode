# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false

import re
import math

class Solution:
    def isPalindrome(self, s):
        # if there are less than two characters in the string, it is a palindrome by default
        if len(s) < 2:
            return True
        # remove all non-alphanumeric characters from the string
        subS = re.sub(r'[^a-zA-Z0-9]', "", s)
        # change entire string to lowercase letters
        lowS = subS.lower()
        # loop through the string
        for i in range(math.floor(len(lowS)/2)):
            # compare the current front character to the character at the matching end position
            # if the two characters do not match, then this is not a palindrome
            if lowS[i] != lowS[len(lowS) - 1 - i]:
                return False
        # once the entire string has been evaluated, it remains that it is a palindrome
        return True

string = "A man, a plan, a canal: Panama!"
s = Solution()
a = s.isPalindrome(string)
print(a)