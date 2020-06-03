# Given a pattern and a string str, find if str follows the same pattern. Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Example 1:
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true

# Example 2:
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false

# Example 4:
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false

# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

class Solution:
    def wordPattern(self, pattern, str):
        # split the string using a space as the delimiter and place in an array
        arr = str.split(" ")
        # if the pattern and the array are different lengths, then the original string did not follow the pattern
        if len(pattern) != len(arr):
            return False
        # zip the pattern and array, creating tuples where each piece of the array corresponds to the place in the pattern
        # create a set of the pattern, the array, and the zipped tuples (sets only retain unique values)
        # compare the lengths of each set
        # if any are different, then the array did not follow the pattern
        # if all lengths are the same, then the array did follow the pattern
        return len(set(zip(pattern, arr))) == len(set(pattern)) == len(set(arr))

pattern = "abba"
str = "cat at att cat"
s = Solution()
a = s.wordPattern(pattern, str)
print(a)