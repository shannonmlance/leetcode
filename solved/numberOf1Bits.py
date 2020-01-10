# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

# Example 1:
# Input: 0000 0000 0000 0000 0000 0000 0000 1011
# Output: 3
# Explanation: The input binary string has a total of three '1' bits.

# Example 2:
# Input: 0000 0000 0000 0000 0000 0000 1000 0000
# Output: 1
# Explanation: The input binary string has a total of one '1' bit.

# Example 3:
# Input: 1111 1111 1111 1111 1111 1111 1111 1101
# Output: 31
# Explanation: The input binary string has a total of thirty-one '1' bits.

# Note:
# Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.

# Follow up:
# If this function is called many times, how would you optimize it?

# input is actually an integer, not the binary as demonstrated in the examples
class Solution:
    def hammingWeight(self, n):
        # establish a variable to count how many '1' bits there are
        count = 0
        # loop until the input integer is zero
        while n != 0:
            # for every loop, increment the count by 1
            count += 1
            # we're going to bit-wise AND the input number and the input number minus one
            # the difference in bits between the input number and the input number minus one:
                # input number: starting on the right of the binary string, find the first '1'. This is the least significant 1. Logically, everything to the right of the least significant 1 must be zeros
                # input number minus one: at the place of the input number's least significant 1, this will be a zero with everything to the right of that place being ones
                # for example:                                                                   v least significant 1
                    # input number =            4,042,322,160 = 1111 0000 1111 0000 1111 0000 1111 0000
                    # input number minus one =  4,042,322,159 = 1111 0000 1111 0000 1111 0000 1110 1111
            # bit-wise AND compares each bit and multiplies them
                # because everything to the left of the least significant 1 in both numbers is identical, it will remain identical after the operation
                # because the least significant 1 and everything to the right of it in both numbers are opposites, all of those places will become zeros
                # for example:
                    # after operation: input number = 4,042,322,144 = 1111 0000 1111 0000 1111 0000 1110 0000
            # we can now repeat the process with the new number, isolating the new least significant 1
            # this process is fast because we can skip any zeros in the original number, so we are only counting ones, which is why no if statement is required
            n &= (n-1)
        return count

n = 11
s = Solution()
a = s.hammingWeight(n)
print(a)