# Given two strings, s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: True

# Example 2:
# Input: s = " foo", t = "bar"
# Output: False

# Example 3:
# Input: s = "paper", t = "title"
# Output: True

# Note:
# You may assume both s and t have the same length.

class Solution:
    def isIsomorphic(self, s, t):
        # zip(s,t) means for each value of s, link the corresponding value of t
        # set() means if two pieces are identical, combine them
        # by comparing the lengths, we can determine how many duplicates there are in each string, and if the duplicates occur at corresponding places
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

class mySolution:
    def isIsomorphic(self, s, t):
        # create two dictionaries, one for each string
        ds = {}
        dt = {}
        # loop through each letter in the strings
        for i in range(len(s)):
            # if the letter in string s is already a key in the s dictionary
            if s[i] in ds:
                # and if the value for that key is not equal to the letter in string t at the same place, then the two strings cannot be isomorphic
                if ds[s[i]] != t[i]:
                    return False
            # if the letter in string t is already a key in the t dictionary
            if t[i] in dt:
                # and if the value for that key is not equal to the letter in string s at the same place, then the two strings cannot be isomorphic
                if dt[t[i]] != s[i]:
                    return False
            # if the letter in both strings are not already keys in the dictionaries
            else:
                # create a key value pair in the s dictionary, setting the key as the letter in string s and the value as the letter in string t
                ds[s[i]] = t[i]
                # create a key value pair in the t dictionary, setting the key as the letter in string t and the value as the letter in string s
                dt[t[i]] = s[i]
        # if the loop completes, then the two strings are isomorphic
        return True

s = "bible"
t = "paper"
sol = Solution()
a = sol.isIsomorphic(s, t)
print(a)