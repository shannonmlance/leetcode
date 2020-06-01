# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example:
# Given n = 5, and version = 4 is the first bad version.
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

class Solution:
    def firstBadVersion(self, n):
        # make recursive call, passing in 1 and the given number of versions as the starting parameters
        c = self.rFindBadVersion(1, n)
        # return the number from the recursive call
        return c
    # recursive binary search method
    def rFindBadVersion(self, s, e):
        # if the given start number is equal to the given end number, return the end number, as this is the first bad version
        if s == e:
            return e
        # find the middle by subtracting the start from the end and dividing the difference, then add the start to the quotient
        m = (e - s)//2 + s
        # make the "api" call
        # if the response is false
        if not self.isBadVersion(m):
            # change the start number to equal the middle number, plus one
            s = m + 1
        # if the response is true
        else:
            # change the end number to equal the middle number
            e = m
        # repeat the recursive call, passing in the updated start and end numbers
        return self.rFindBadVersion(s, e)
    # boolean "api" call that returns whether the given version is the first bad version
    def isBadVersion(self, v):
        # define the first bad version's number
        firstBadVersion = 46
        # if the given version is less than the first bad version, return false
        if v < firstBadVersion:
            return False
        # if the given version is not less than the first bad version, return true
        else:
            return True

n = 45
s = Solution()
a = s.firstBadVersion(n)
print(a)
