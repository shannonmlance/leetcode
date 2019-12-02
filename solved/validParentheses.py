# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

# Example 4:
# Input: "([)]"
# Output: false

# Example 5:
# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s):
        # if the string is empty, then the parentheses are valid by default
        if len(s) == 0:
            return True
        # if the string contains only one symbol, then the parentheses must be invalid, since valid parentheses come in pairs
        if len(s) == 1:
            return False
        # initialize a dictionary for matching pairs of open and closed parentheses
        d = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        # if the string contains only two symbols, they are either a match or not
        if len(s) == 2:
            # reference the dictionary to validate that the first symbol is an open parentheses
            if s[0] in d:
                # if the key and value match, this is a valid set
                if s[1] == d[s[0]]:
                    return True
                # if the key and value do not match, this is an invalid set
                else:
                    return False
            # if the first symbol is not an open parentheses, then this is invalid
            else:
                return False
        # initialize a stack for tracking the order of open parenthesis
        stack = []
        # iterate through the string
        for i in s:
            # if the symbol is a key in the dictionary, it is an open parentheses
            if i in d:
                # add the matching closed parentheses to the stack
                stack.append(d[i])
            # if the symbol is not a key in the dictionary, it is a closed parentheses
            else:
                # if the stack is empty, then we have more closed parentheses than open parentheses and the string is invalid
                if len(stack) == 0:
                    return False
                # remove the last symbol from the stack
                v = stack.pop()
                # if it doesn't match the current symbol, then the order of parentheses is invalid
                if v != i:
                    return False
        # if there are still symbols in the stack, then we have more open parentheses than closed parentheses and the string is invalid
        if len(stack) > 0:
            return False
        # the string is valid
        return True

s = "][][]["
sol = Solution()
a = sol.isValid(s)
print(a)

# use a stack to keep track of correct order
# use a dictionary to match the types of characters, using open characters as keys and closing characters as values
# iterate through the string
# for each symbol, if it's in the dictionary, place it's value in the stack
# if it's not in the dictionary, check the stack to see if that's the correct symbol