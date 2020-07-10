# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Input: "hello"
# Output: "holle"

# Example 2:
# Input: "leetcode"
# Output: "leotcede"

# Note:
# The vowels does not include the letter "y".

class Solution:
    def reverseVowels(self, s):
        # list all vowels, both lower and upper casw
        vowels = "aeiouAEIOU"
        # initiate two lists
        s1 = []
        s2 = []
        # initiate two pointers, one at the beginning of the string, abd one at the end of the string
        i = 0
        j = len(s) - 1
        # loop as long as the beginning pointer is on the left of the end pointer
        while i < j:
            # if the beginning pointer is a vowel
            if s[i] in vowels:
                # and if the end pointer is a vowel
                if s[j] in vowels:
                    # add the end pointer to the first list
                    s1.append(s[j])
                    # add the beginning pointer to the second list
                    s2.append(s[i])
                    # increment the beginning pointer
                    i += 1
                    # decrement the end pointer
                    j -= 1
                # if the end pointer is not a vowel
                else:
                    # add the end pointer to the second list
                    s2.append(s[j])
                    # decrement the end pointer
                    j -= 1
            # if the beginning pointer is not a vowel
            else:
                # add the beginning pointer to the first list
                s1.append(s[i])
                # increment the beginning pointer
                i += 1
        # if the beginning pointer and the end pointer are pointing to the same place
        if i == j:
            # add the end pointer to the second list
            s2.append(s[j])
        # initiate an empty string
        string = ""
        # loop through the first list
        for i in range(len(s1)):
            # add each value to the string
            string += s1[i]
        # loop backwards through the second list
        for i in range(len(s2) - 1, -1, -1):
            # add each value to the string
            string += s2[i]
        # return the modified string
        return string

s = "palindrome"
sol = Solution()
a = sol.reverseVowels(s)
print(a)
