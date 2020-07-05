# Write a function that reverses a string. The input string is given as an array of characters char[]. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory. You may assume all the characters consist of printable ascii characters.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

class Solution:
    def reverseString(self, s):
        # loop through half of the given array
        for i in range(len(s)//2):
            # store the current value in the array in a temp variable
            t = s[i]
            # change the current value in the array to equal the value of the corresponding place at the end of the array
            s[i] = s[len(s) - 1 - i]
            # change the value of the corresponding place at the end of the array to equal the temp variable's value
            s[len(s) - 1 - i] = t
        return

s = ["h", "e", "l", "l", "o", "p"]
sol = Solution()
sol.reverseString(s)
print(s)