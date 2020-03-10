# Given two strings, s and t, write a function to determine if t is an anagram of s.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Note:
# You may assume the string contains only lowercase alphabets.

from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        # if s and t are different lengths, then t is not an anagram of s
        if len(s) != len(t):
            return False
        # create a dictionary for each string with each letter from the string as the key and the frequency of each letter as the corresponding value
        sCount = Counter(s)
        tCount = Counter(t)
        # subtract the second dictionary from the first dictionary
        # if there is value in the remainder, then t is not an anagram of s
        return not sCount - tCount

class mySolution:
    def isAnagram(self, s, t):
        # initiate a dictionary
        d = {}
        # loop through s
        for i in range(len(s)):
            # if the letter in s is already in the dictionary, increment that letter's count
            if s[i] in d:
                d[s[i]] += 1
            # if the letter in s is not in the dictionary, add it with the letter as the key and a value of 1
            else:
                d[s[i]] = 1
        # loop through t
        for i in range(len(t)):
            # if the letter in t is already in the dictionary, decrement that letter's count
            if t[i] in d:
                d[t[i]] -= 1
            # if the letter in t is not in the dictionary, then t is not an anagram of s
            else:
                return False
            # if the letter in t is in the dictionary and has value of zero, remove it from the dictionary
            if d[t[i]] == 0:
                d.pop(t[i])
        # if the dictionary is empty, t is an anagram of s
        if d == {}:
            return True
        # if the dictionary is not empty, t is not an anagram of s
        return False

s = "anagramz"
t = "nagaramp"
sol = Solution()
a = sol.isAnagram(s, t)
print(a)