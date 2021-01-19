# Write a function that reverses a string. The input string is given as an array of characters char[]. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory. You may assume all the characters consist of printable ascii characters.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

class Solution:
    def reverseString(self, s):
        # set iterator
        i = 0
        # loop through half of the array
        while i < len(s)/2:
            # swap the current value with the corresponding value at the end of the array
            temp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = temp
            # increment
            i += 1
        return None

s = ["h","e","l","l","o"]
sol = Solution()
sol.reverseString(s)
print(s)