# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

# works just fine
class myFirstSolution:
    def sortedSquares(self, nums):
        sortedSquaredArray = []
        for n in nums:
            n = n * n
            self.addSquares(sortedSquaredArray, n, 0, len(sortedSquaredArray))
        return sortedSquaredArray
    def addSquares(self, sortedSquaredArray, n, start, end):
        middle = ((end - start) // 2) + start
        if start >= end:
            sortedSquaredArray.insert(start, n)
            return
        if middle >= end:
            sortedSquaredArray.append(n)
            return
        if n > sortedSquaredArray[middle]:
            self.addSquares(sortedSquaredArray, n, middle + 1, end)
        elif n <= sortedSquaredArray[middle]:
            self.addSquares(sortedSquaredArray, n, start, middle)
        return

class Solution:
    def sortedSquares(self, nums):
        front = 0
        back = len(nums) - 1
        while back >= 0:
            f = nums[front] * nums[front]
            b = nums[back] *  nums[back]
            if f > b:
                nums.pop(front)
                nums.insert(back, f)
                back -= 1
            else:
                nums[back] = b
                back -= 1
        return nums


nums = [-16,-4,-2,-1,0,1,3,11,16]
s = Solution()
a = s.sortedSquares(nums)
print(a)