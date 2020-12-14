# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer. The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit. You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# Example 3:
# Input: digits = [0]
# Output: [1]

# Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9

class Solution:
    def plusOne(self, digits):
        # set index marker at the end of the array
        i = len(digits) - 1
        # call recursive method, passing in array and index marker
        self.rPlusOne(digits, i)
        return digits
    def rPlusOne(self, digits, i):
        # if the digit at the index marker is less than 9
        if digits[i] < 9:
            # increment the digit at the index marker
            digits[i] += 1
        # if the digit at the index marker is 9
        else:
            # set the digit at the index marker equal to 0
            digits[i] = 0
            # decrement the index marker
            i -= 1
            # if the index marker is negative
            if i < 0:
                # insert a 1 at the beginning of the array
                digits.insert(0, 1)
            # if the index marker is within the array
            else:
                # recursively call the method, passing in the modified array and the new index marker
                self.rPlusOne(digits, i)
        return digits

digits = [8,9]
s = Solution()
a = s.plusOne(digits)
print(a)