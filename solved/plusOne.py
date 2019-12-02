# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

class Solution:
    def plusOne(self, digits):
        # if the last digit is equal to 9, adding 1 will cause overflow of this digit's index
        if digits[len(digits)-1] == 9:
            # if there is only one digit in the array
            if len(digits) == 1:
                # change it to a 1
                digits[0] = 1
            # if there are more digits in the array
            else:
                # remove the last digit from the array
                digits.pop()
                # recursively call method, passing in the shortened array
                digits = self.plusOne(digits)
            # add a 0 to the end of the array
            digits.append(0)
        # if the last digit is not equal to 9,
        else:
            # add 1 to that value
            digits[len(digits)-1] += 1
        # return the modified array
        return digits

class Solution:
    def plusOne(self, digits):
        if digits[len(digits)-1] == 9:
            if len(digits) == 1:
                digits[0] = 1
            else:
                digits.pop()
                digits = self.plusOne(digits)
            digits.append(0)
        else:
            digits[len(digits)-1] += 1
        return digits

digits = [9,9,9]
s = Solution()
a = s.plusOne(digits)
print(a)

# if the last digit is equal to 9
    # make it equal to 0
    # if there is a digit immediately prior
        # repeat process for the digit immediately prior
    # else, insert a 1 at the beginning of the array
# else, add one to the last digit