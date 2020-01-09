# Reverse bits of a given 32 bits unsigned integer.

# Example 1:
# Input: 0000 0010 1001 0100 0001 1110 1001 1100
# Output: 0011 1001 0111 1000 0010 1001 0100 0000
# Explanation: The input binary string [input] represents the unsigned integer 43261596, so return 964176192 which its binary representation is [output].

# Example 2:
# Input: 1111 1111 1111 1111 1111 1111 1111 1101
# Output: 1011 1111 1111 1111 1111 1111 1111 1111
# Explanation: The input binary string[input] represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is [output].

# Note:
# Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents teh signed integer -3 and the output represents the signed integer -1073741825.

# Follow up:
# If this function is called many times, how would you optimize it?

# input is actually an integer, not the binary as demonstrated in the examples
# output is also an integer, not the binary as demonstrated in teh examples
class Solution:
    def reverseBits(self, n):
        # create variable to store the binary format of the input integer
        # bin(n) returns a string with the binary value of the input integer, with no leading zeros, and the binary indicator of 0b
        # [2:] removes the binary indicator
        # zfill(32) adds leading zeros to the binary string, up to 32 characters
        num = bin(n)[2:].zfill(32)
        # create a variable to store the reversed binary string
        # num[::-1] reverses the binary string
        # int(<string>, 2) casts the given string into an integer, using a base 2 (binary)
        n = int(num[::-1], 2)
        return n

n = 2147483648
s = Solution()
a = s.reverseBits(n)
print(a)